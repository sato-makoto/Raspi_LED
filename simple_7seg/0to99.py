#!/usr/bin/env python

from sys import argv
from time import sleep
from time import time
import RPi.GPIO as GPIO
import on_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
  ltime = float(argv[1])
  repeat_time = int(argv[2])
except:
  ltime = 0.5
  repeat_time = 2

repeat_time, cont = on_off.for_back(repeat_time)

swaptime = 0.001
number = 0
allnum = 100
light_led = []
for x in range(repeat_time):
   for y in range(allnum)[::cont]:
     light_led = on_off.right_left(y)
     btime = time()
     etime = 0
     while btime + ltime > etime:
       for z in on_off.right, on_off.left:
         if z == on_off.right:
           e = 0
         else:  
           e = 1
         on_off.led_on(light_led[e], z) 
         sleep(swaptime)
         on_off.led_off(light_led[e], z) 
       etime = time()

GPIO.cleanup()

