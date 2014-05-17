#!/usr/bin/env python
# -*- coding: utf-8 -*-

# led one to another 
# first parameter is led on time
# second parameter is times of led cycle
# when second parameter is less than 0;
# circle reversed

from sys import argv
import time
import RPi.GPIO as GPIO
from twenty_on_off import led_on
from twenty_on_off import led_off
from twenty_on_off import light_num
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

all_led = len(light_num)
try:
  ltime = float(argv[1])
  repeat_time = int(argv[2])
except:
  ltime = 0.05
  repeat_time = 5

if repeat_time < 0:
  cont = -1
  repeat_time = abs(repeat_time)
else:
  cont = 1

for i in range(repeat_time):
  for led in range(all_led)[::cont]:
    led_on(led)
    time.sleep(ltime)
    led_off(led)

GPIO.cleanup()
