#!/usr/bin/env python
# Referenced from Raspberry PI User Guide
# http://goo.gl/xCJcCH
# first edition P.183
# changed somewhere 

import RPi.GPIO as GPIO
port = 28
GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.IN)

count = 0
while True:
  red_button = GPIO.input(port)
  if red_button == False:
   count += 1
   print "press", count
   while red_button == False:
       red_button = GPIO.input(port)

