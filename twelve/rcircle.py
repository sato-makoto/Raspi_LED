#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import time
import RPi.GPIO as GPIO
from twelve_led_on_off import led_on
from twelve_led_on_off import led_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
  ltime = float(argv[1])
  repeat_time = int(argv[2])
except:
  ltime = 0.05
  repeat_time = 10

for i in range(repeat_time):
  for led in range(11,-1, -1):
    led_on(led)
    time.sleep(ltime)
    led_off(led)

GPIO.cleanup()
