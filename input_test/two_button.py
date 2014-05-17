#!/usr/bin/env python
# -*- coding: utf-8 -*-

# check GPIO 28 and 31
# when GPIO is False
# print button pressed
# It will check both GPIO
# for future.


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def input_check(port):
  button = GPIO.input(port)
  return (button, port)

ports = [28, 30, 31]
GPIO.setup(ports[0], GPIO.IN)
GPIO.setup(ports[1], GPIO.OUT)
GPIO.setup(ports[2], GPIO.IN)
GPIO.output(ports[1], GPIO.HIGH)

while True:
  for port in ports[::2]:
    check = input_check(port)
    if check[0] == False:
      if port == ports[0]:
        print '赤い釦が押されました'
      elif port == ports[2]:
        print '緑の釦が押されました'
      while check[0] == False:
        check = input_check(port)
