#!/bin/sh

# display "47"

first=18
second=17
a=0; b=1; c=2; d=3; e=4; f=5; g=6; h=7
left="$b $d $f $g"
right="$b $f $g $h"

gpio mode $first out
gpio mode $second out

for times in `seq 100`
do
  gpio write  $first 1
  for z in $left; do gpio mode $z out; done
  for z in $left; do gpio mode $z in; done
  gpio write $first 0
  gpio write $second 1
  for z in $right; do gpio mode $z out; done
  for z in $right; do gpio mode $z in; done
  gpio write $second 0
done
