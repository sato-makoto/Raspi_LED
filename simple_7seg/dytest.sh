#!/bin/sh

# display "47"

first=18
second=17
a=0; b=1; c=2; d=3; e=4; f=5; g=6; h=7
left="$b $d $f $g"
right="$b $f $g $h"
common="$b $d $f $g $h"
diff1=$d
diff2=$h

gpio reset

for x in $first $second
do
  gpio mode $x out
  gpio write $x 1
  gpio mode $x in
done

for y in $common
  do gpio mode $y out
done

for times in `seq 100`
do
  gpio mode $diff2 in
  gpio mode $diff1 out
  gpio mode $first out
  gpio mode $first in
  gpio mode $diff1 in
  gpio mode $diff2 out
  gpio mode $second out
  gpio mode $second in
done

gpio reset
