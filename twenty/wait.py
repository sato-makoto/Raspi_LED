#!/usr/bin/env python
# -*- coding: utf-8 -*-

# count python loop time 
# led on , count start, loop, count end,  led off 

from sys import argv
import time
import RPi.GPIO as GPIO
from twenty_on_off import led_on
from twenty_on_off import led_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
  repeat_time = int(argv[1])
except:
  print "No time to wait"
  exit(1)

myport = 5
start = time.time()
led_on(myport)
for i in range(repeat_time):
  pass

end = time.time()
print round(end - start, 2)
led_off(myport)
led_on(myport + 1)
time.sleep(3)
led_off(myport + 1)

GPIO.cleanup()
