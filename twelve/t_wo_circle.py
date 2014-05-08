#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from time import sleep
import RPi.GPIO as GPIO
import twelve_led_on_off as on_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
  ltime = float(argv[1])
  repeat_time = int(argv[2])
except:
  ltime = 0.001
  repeat_time = 3

mylight = on_off.light_num
for x in range(repeat_time): 
  for y in range(12):
    l1, l2 = mylight[0], mylight[2]
    for z in range(300):
      on_off.led_on(l1)
      sleep(ltime)
      on_off.led_off(l1)
      on_off.led_on(l2)
      sleep(ltime)
      on_off.led_off(l2)
    mylight.append(mylight.pop(0))



GPIO.cleanup()
