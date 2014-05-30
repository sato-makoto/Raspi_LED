#!/bin/sh
# light 39
# use sysfs

SYS=/sys/class/gpio
num3=3
num9=9
left=29
right=28
sleep=0.001
times=500

a=17; b=18; c=27; d=22; e=23; f=24; g=25; h=4
common="$d $e $f $g $h" 
dif=$b

for x in  $common $b $left $right
do 
  echo $x > ${SYS}/export
done

for x in $common $left $right
do
  echo out > ${SYS}/gpio${x}/direction
done

for x in `seq $times`
do 
  echo out > ${SYS}/gpio${dif}/direction
  echo 1 >  ${SYS}/gpio${right}/value
  sleep $sleep
  echo 0 >  ${SYS}/gpio${right}/value
  echo in > ${SYS}/gpio${dif}/direction
  echo 1 >  ${SYS}/gpio${left}/value
  sleep $sleep
  echo 0 >  ${SYS}/gpio${left}/value
done

for x in $common $b $left $right
do 
  echo in > ${SYS}/gpio${x}/direction
  echo $x > ${SYS}/unexport
done
