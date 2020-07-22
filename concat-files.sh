#!/bin/bash
cat filter1/*.txt > simpsons-unformatted.txt
# change to utf-8
iconv -f iso-8859-1 -t utf-8 < simpsons-unformatted.txt > simpsons.txt
# rm simpsons-unformatted.txt
