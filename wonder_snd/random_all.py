#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 
from time import sleep
from  random import seed, shuffle, random

from port_pin_on_off import on, off, clean, plist
# import RPi.GPIO as GPIO

try:
  roundtime = int(argv[1])
except:
  print "How many time?"
  exit(1)

# GPIO.setmode(GPIO.BCM)

shuffle_list = [1,2,3,4,5,6]
for i in range(roundtime):
  seed()
  shuffle(shuffle_list)
  for port in shuffle_list:
    on(port)
    roundsectime = random() * 5
    print(port,  round(roundsectime, 2))
    sleep(roundsectime)
    off(port)

clean()
