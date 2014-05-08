#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 
import time
import RPi.GPIO as GPIO
import random

try:
  repeat_time = int(argv[2])
except:
  repeat_time = 10

sleeptime = 1.0/repeat_time
# use port 29-31
random.seed()
ports = [28,29,30]
in_port = ports.pop(random.randint(0,2))
out_port = ports.pop(random.randint(0,1))
port = ports[0]
print in_port, out_port, port

print \
  '{} times by {} seconds.'\
    .format(repeat_time, sleeptime)
GPIO.setmode(GPIO.BCM)

GPIO.setup(in_port, GPIO.IN)
GPIO.setup(out_port, GPIO.OUT)
GPIO.setup(port, GPIO.OUT)


for i in range(repeat_time):
  GPIO.output(port,GPIO.HIGH)
  time.sleep(sleeptime)
  GPIO.output(port,GPIO.LOW)
  time.sleep(sleeptime)
GPIO.cleanup()
