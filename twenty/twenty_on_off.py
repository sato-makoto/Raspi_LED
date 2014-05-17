#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

# use port 29-31
from time import sleep
ports = [17, 18, 27, 22, 4]
light_num = [
   0, 1, 2, 3, 4, 5, 
   6, 7, 8, 9, 10, 11,
   12, 13, 14, 15, 16,
   17, 18, 19]
p0, p1, p2, p3, p4, = ports
leds = [
[p0, p4], [p4, p0], 
[p3, p4], [p4, p3], 
[p1, p4], [p3, p0], 
[p0, p3], [p1, p0], 
[p0, p1], [p4, p1], 
[p1, p3], [p3, p1], 
[p2, p0], [p0, p2], 
[p2, p4], [p2, p1], 
[p1, p2], [p2, p3], 
[p3, p2], [p4, p2]] 

def led_on(num):
  led = leds[num] 
  GPIO.setup(led[0], GPIO.OUT)
  GPIO.setup(led[1], GPIO.OUT)
  GPIO.output(led[0], GPIO.HIGH)

def led_off(num):
  led = leds[num] 
  GPIO.setup(led[0], GPIO.OUT)
  GPIO.output(led[0], GPIO.LOW)
  GPIO.setup(led[0], GPIO.IN)
  GPIO.setup(led[1], GPIO.IN)
