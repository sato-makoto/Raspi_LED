#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 
import time
import RPi.GPIO as GPIO
import random

try:
  out_port = int(argv[1])
  low_port = int(argv[2])
except:
  out_port = 28
  low_port = 31

repeat_time = 3
sleep_time =  0.5

# use port 29-31
ports = [30,28,29,31]
ports.pop(ports.index(out_port))
ports.pop(ports.index(low_port))
[in_port1, in_port2] = ports
GPIO.setmode(GPIO.BCM)

GPIO.setup(low_port, GPIO.OUT)
GPIO.setup(low_port, GPIO.LOW)
GPIO.setup(in_port1, GPIO.IN)
GPIO.setup(in_port2, GPIO.IN)
GPIO.setup(out_port, GPIO.OUT)


for i in range(repeat_time):
  GPIO.output(out_port,GPIO.HIGH)
  time.sleep(sleep_time)
  GPIO.output(out_port,GPIO.LOW)
  time.sleep(sleep_time)
GPIO.cleanup()
