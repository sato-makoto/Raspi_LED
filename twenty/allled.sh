#!/bin/bash
source ./galilas.txt

if [ -z "$1" ]; then
  STIME=0.5
else
  STIME=$1
fi

for x in `seq 0 19`
do 
  ledon $x
  sleep $STIME
done

gpio reset
