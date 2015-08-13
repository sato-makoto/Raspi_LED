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

sleeptime = 3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

p_port = 12
g_port = 17

GPIO.setup(g_port, GPIO.OUT)
GPIO.setup(p_port, GPIO.OUT)

GPIO.output(p_port,GPIO.HIGH)
time.sleep(sleeptime)
GPIO.output(p_port,GPIO.LOW)
GPIO.setup(p_port, GPIO.IN)
GPIO.setup(g_port, GPIO.IN)

GPIO.cleanup()
