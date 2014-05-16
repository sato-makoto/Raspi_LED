#!/usr/bin/env python
# Referenced from Raspberry PI User Guide
# http://goo.gl/xCJcCH
# first edition P.183
# changed somewhere 

# print "press .time." when pushed green button.
# Ctrl-C to stop this program.
# run it as super user.

import RPi.GPIO as GPIO

uport = 31
port = 30
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port, GPIO.IN)
GPIO.setup(uport, GPIO.OUT)
GPIO.output(uport,GPIO.HIGH)

count = 0
while True:
  green_button = GPIO.input(port)
  if green_button == False:
   count += 1
   print "press", count
   while green_button == False:
       green_button = GPIO.input(port)
