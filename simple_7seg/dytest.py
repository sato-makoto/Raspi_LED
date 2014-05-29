#!/usr/bin/env python

# display "72" for 10 seconds.

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

times = 500
wait = 0.01

# 7 segment ports
a, b, c, d, e, f, g, h = 17, 18, 27, 22, 23, 24, 25, 4
# from 0 to 9 LED
led_array= [  
  [a, b, e, f, g, h], 
  [f, g], 
  [a, d, e, g, h], 
  [d, e, f, g, h], 
  [b, d, f, g], 
  [b, d, e, f, h], 
  [a, b, d, e, f, h], 
  [b, f, g, h], 
  [a, b, d, e, f, g, h], 
  [b, d, e, f, g, h] ]

# right port
first = 28
# left port
second = 29 

for x in first, second:
  GPIO.setup(x, GPIO.OUT)

for x in range(times):
  for y in led_array[2]:
    GPIO.setup(y, GPIO.OUT)
  GPIO.output(first, GPIO.HIGH)
  sleep(wait)
  GPIO.output(first, GPIO.LOW)
  for y in led_array[2]:
    GPIO.setup(y, GPIO.IN)
  for z in led_array[7]:
    GPIO.setup(z, GPIO.OUT)
  GPIO.output(second, GPIO.HIGH)
  sleep(wait)
  for z in led_array[7]:
    GPIO.setup(z, GPIO.IN)
  GPIO.output(second, GPIO.LOW)
GPIO.cleanup()

