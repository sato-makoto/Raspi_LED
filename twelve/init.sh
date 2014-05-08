#!/usr/bin/sh

for x in `seq 17 20`
do
  gpio mode $x in
done
