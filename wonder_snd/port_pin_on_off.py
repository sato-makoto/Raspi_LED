#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

# sound on, off, etc.
# need to import on, off, aoff, clean
# argumet is one of 1,2,3,4,5,6
# wrong argument become 1

"""
PORT  JP
24    1
17    2
18    3
27    4
22    5
23    6

"""
ptupple = (24, 17, 18, 27, 22, 23)
hlist = set([])

GPIO.setmode(GPIO.BCM)

def check(pin):
  if 0 < pin < 7:
    return int(pin)
  else:
    return 1

def on(pin):
  pin = check(pin)
  pin = pin - 1
  GPIO.setup(ptupple[pin], GPIO.OUT)
  GPIO.output(ptupple[pin], GPIO.HIGH)
  hlist.add(ptupple[pin])

def off(pin):
  pin = check(pin)
  pin = pin - 1
  GPIO.output(ptupple[pin], GPIO.LOW)
  hlist.remove(ptupple[pin])

def aoff():
  for num in hlist:
    GPIO.output(num, GPIO.LOW)
  hlist.clear()

def clean():
  GPIO.cleanup()
