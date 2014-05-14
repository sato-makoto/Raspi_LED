#!/usr/bin/env python
# -*- coding: utf-8 -*-

# blink red LEDs and green LEDs

from sys import argv
import time
import RPi.GPIO as GPIO
from twenty_on_off import led_on
from twenty_on_off import led_off
from twenty_on_off import light_num
# from twenty_on_off import leds
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

all_led = len(light_num)
try:
  ltime = float(argv[1])
  repeat_time = int(argv[2])
except:
  ltime = 0.0005
  repeat_time = 30

odd = light_num[0::2]
even = light_num[1::2]
one_cycle = 80

for x in range(repeat_time):
  for i in range(one_cycle):
    for led in odd:
      led_on(led)
      time.sleep(ltime)
      led_off(led)
  for j in range(one_cycle):
    for led in even:
      led_on(led)
      time.sleep(ltime)
      led_off(led)

GPIO.cleanup()
