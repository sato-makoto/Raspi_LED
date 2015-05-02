#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 
import time
import RPi.GPIO as GPIO

"""
PORT  JP
24    1
17    2
18    3
22    5
23    6
27    4

"""
try:
  sleeptime = int(argv[2])
except:
  print "no port"
  print "17 18 22 23 24 27"
  exit(1)

port = int(argv[1])

print \
  '{} port by {} seconds.'\
    .format(port, sleeptime)
GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)

GPIO.output(port,GPIO.HIGH)
time.sleep(sleeptime)
GPIO.output(port,GPIO.LOW)
GPIO.cleanup()