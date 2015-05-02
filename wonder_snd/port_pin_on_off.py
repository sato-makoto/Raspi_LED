#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

"""
PORT  JP
24    1
17    2
18    3
27    4
22    5
23    6

"""

plist = [24, 17, 18, 27, 22, 23]
hlist = set([])

GPIO.setmode(GPIO.BCM)

def on(pin):
  pin = pin - 1
  GPIO.setup(plist[pin], GPIO.OUT)
  GPIO.output(plist[pin], GPIO.HIGH)
  hlist.add(plist[pin])

def off(pin):
  pin = pin - 1
  GPIO.output(plist[pin], GPIO.LOW)
  hlist.remove(plist[pin])

def aoff():
  for num in hlist:
    GPIO.output(num, GPIO.LOW)
  hlist.clear()

def clean():
  GPIO.cleanup()
