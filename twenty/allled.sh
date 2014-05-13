#!/bin/bash
source ./galilas.txt

for x in `seq 0 19`
do 
  ledon ${led_array[$x]}
  echo ${led_array[$x]}
  sleep 1
done

gpio reset
