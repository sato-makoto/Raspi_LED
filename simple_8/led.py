#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 
import time
import RPi.GPIO as GPIO

try:
  repeat_time = int(argv[1])
except:
  repeat_time = 10

sleeptime = 5.0/repeat_time
port = 18
print \
  '{} times by {} seconds.'\
    .format(repeat_time, sleeptime)
GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)

for i in range(repeat_time):
  GPIO.output(port,GPIO.HIGH)
  time.sleep(sleeptime)
  GPIO.output(port,GPIO.LOW)
  time.sleep(sleeptime)
GPIO.cleanup()
