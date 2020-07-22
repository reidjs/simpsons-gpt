#!/bin/bash
i="0"
while [ $i -lt 10 ] 
do
	docker cp e1be5941ab01:/gpt-2/output .
	git add .
	git commit -m "Pull output from docker"
	git push
	i=$[$i+1]
	echo $i
	sleep 1800 
done
