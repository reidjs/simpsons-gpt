#!/bin/bash
while true
do
	docker cp e1be5941ab01:/gpt-2/output .
	git add .
	git commit -m "Pull output from docker"
	git push
	sleep 60
done
