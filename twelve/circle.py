#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import time
import RPi.GPIO as GPIO
from twelve_led_on_off import led_on
from twelve_led_on_off import led_off
from twelve_led_on_off import light_num
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

all_led = len(light_num)
try:
  ltime = abs(float(argv[1]))
  repeat_time = int(argv[2])
except:
  ltime = 0.05
  repeat_time = 10

for i in range(repeat_time):
  for led in range(all_led):
    led_on(led)
    time.sleep(ltime)
    led_off(led)

GPIO.cleanup()
