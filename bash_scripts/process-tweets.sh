#!/bin/bash

python3 process-tweets.py < OutputFiles/tweets.jsonl > OutputFiles/tweets.info.txt
xargs < OutputFiles/tweets.info.txt curl -IL | egrep -i "(^location:)" > OutputFiles/finalURI.txt
sed -e 's/location: //g' -e 's/Location: //g' -e '/^\//d' -e 's/youtube//g' -e 's/youtu.be//g' OutputFiles/finalURI.txt > OutputFiles/rawOutput.txt
sort OutputFiles/rawoutput.txt | uniq > OutputFiles/uniqueURI.txt