#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import time
import RPi.GPIO as GPIO
from six_led_on_off import led_on
from six_led_on_off import led_off

ltime = 0.5
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ports = [28,29,30]
for port in ports:
  led_on(ports[0], ports[1],ports[2])
  print(ports[0], ports[1],ports[2])
  time.sleep(ltime)
  led_off(ports[2])
  led_on(ports[0], ports[2],ports[1])
  print(ports[0], ports[2],ports[1])
  time.sleep(ltime)
  led_off(ports[2])
  ports.insert(2,ports.pop(0))

GPIO.cleanup()
