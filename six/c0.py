#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
import RPi.GPIO as GPIO
from six_led_on_off import led_on
from six_led_on_off import led_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
  repeat_time = int(argv[1])
except:
  repeat_time = 3

for i in range(repeat_time):
  for led in range(6):
    led_on(led)
    led_off(led)

GPIO.cleanup()
