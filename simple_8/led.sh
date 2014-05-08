#!/usr/bin/sh
ON=1
OFF=0
if [ -z $1 ]; then
  NUM=0.5
else
  NUM=$1
fi
  

for x in 7 0 1 3 4 5 6 2 
  do
    gpio mode $x out
    gpio write $x $ON
    sleep $NUM
    gpio write $x $OFF
  done
