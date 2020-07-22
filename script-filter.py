import glob
import os
import re
import codecs
import sys  
reload(sys)
# https://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte
sys.setdefaultencoding('Cp1252')

path='./episodes/'
fileNames = glob.glob('./episodes/*.txt')
# fileNames = glob.glob('./episodes/8F17.txt')
for fileName in fileNames:
  with open(fileName) as file:
    line = file.readline()
    started = False
    foundStart = False
    text = ''
    while line:
      if (line.find("> Quotes ") >= 0):
        # print("starting", line)
        foundStart = True
      if (started and line.find("=======") >= 0):
        # print ('ending', line)
        newFileName = fileName.split('/')[-1]
        f = open('filter1/' + newFileName, 'w')
        # with codecs.open('filter1/' + newFileName, 'w', encoding='utf-8') as f:
        text += '\n<|endoftext|>\n'
        f.write(text)
        break
      if (started):
        text += line
      if (foundStart and line.find("=======") >= 0):
        # print('next', line)
        foundStart = False
        started = True
      #  print("Line {}: {}".format(cnt, line.strip()))
      line = file.readline()