#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import time
import RPi.GPIO as GPIO
from six_led_on_off import led_on
from six_led_on_off import led_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#leds = [[28, 29, 30], [28, 30, 29],
#  [29, 28, 30], [29, 30, 28],
#  [30, 29, 28], [30, 28, 29]]

try:
  ltime = abs(float(argv[1]))
  repeat_time = int(argv[2])
except:
  ltime = 0.1
  repeat_time = 3

for i in range(repeat_time):
  for led in range(6):
    led_on(led)
    time.sleep(ltime)
    led_off(led)

GPIO.cleanup()
