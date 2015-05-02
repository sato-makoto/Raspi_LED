#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 
import time
import random
import RPi.GPIO as GPIO

try:
  roundtime = int(argv[1])
except:
  print "How many time?"
  exit(1)

GPIO.setmode(GPIO.BCM)

for i in range(roundtime):
  ports = [17, 18, 22, 23, 24, 27]
  random.seed()
  random.shuffle(ports)
  for port in ports:
    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, GPIO.HIGH)
    roundsectime = random.random() * 0.5
    print(port, round(roundsectime, 2))
    time.sleep(roundsectime)
    GPIO.output(port ,GPIO.LOW)

GPIO.cleanup()
