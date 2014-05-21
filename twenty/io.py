#!/usr/bin/env python
# -*- coding: utf-8 -*-

# led one to another 
# first parameter is led on time
# second parameter is times of led cycle
# when second parameter is less than 0;
# circle reversed
# when press red button
# led circle quicker
# when press green button
# led circle slower

from sys import argv
import time
import RPi.GPIO as GPIO
from twenty_on_off import led_on
from twenty_on_off import led_off
from twenty_on_off import light_num
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

all_led = len(light_num)
try:
  repeat_time = int(argv[1])
except:
  repeat_time = 50

if repeat_time < 0:
  cont = -1
  repeat_time = abs(repeat_time)
else:
  cont = 1

def input_check(port):
  button = GPIO.input(port)
  return (button)

input_ports = [28, 30, 31]
GPIO.setup(input_ports[0], GPIO.IN)
GPIO.setup(input_ports[1], GPIO.OUT)
GPIO.setup(input_ports[2], GPIO.IN)
GPIO.output(input_ports[1], GPIO.HIGH)
inputwait = 5000
ratio = 1.5
high_thresh = 2
low_thresh = 500000

for i in range(repeat_time):
  for led in range(all_led)[::cont]:
    led_on(led)
    for t in range(inputwait):
      for port in input_ports[::2]:
        check = input_check(port)
        if check == False:
          if port == input_ports[0]:
            if inputwait > high_thresh:
              inputwait = int(inputwait / ratio)
          elif port == input_ports[2]:
            if inputwait < low_thresh:
              inputwait = int(inputwait * ratio)
          while check == False:
            check = input_check(port)
    led_off(led)

GPIO.cleanup()
