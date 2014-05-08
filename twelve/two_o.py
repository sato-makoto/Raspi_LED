#!/usr/bin/env python

# light 
# 0-1, 
# 0-2, 
# 1-2,
# 1-3,
# 2-3, 
# 2-4
# ...

from sys import argv
from time import sleep
import RPi.GPIO as GPIO
import twelve_led_on_off as on_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
  ltime = int(argv[1])
  repeat_time = int(argv[2])
except:
  ltime = 20
  repeat_time = 3

mylight = on_off.light_num[:]

def twolight(first, second, stime):
  for w in range(ltime):
    for x in (first, second):
      on_off.led_on(x)
      sleep(stime)
      on_off.led_off(x)
      sleep(stime)

for y in range(repeat_time):
  for z in range(12):
    twolight(mylight[0], mylight[1], 0.005)
    twolight(mylight[0], mylight[2], 0.002)
    mylight.append(mylight.pop(0))
  
GPIO.cleanup()
