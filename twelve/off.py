#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import time
import RPi.GPIO as GPIO
from twelve_led_on_off import led_on
from twelve_led_on_off import led_off
import twelve_led_on_off as on_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

myleds = on_off.ports
for led in myleds:
  GPIO.setup(led,GPIO.OUT)
  GPIO.output(led, GPIO.LOW)
  GPIO.setup(led, GPIO.IN)
  time.sleep(0.01)

GPIO.cleanup()
