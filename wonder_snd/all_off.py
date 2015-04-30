#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

ports = [17, 18, 22, 23, 24, 27]

GPIO.setmode(GPIO.BCM)
for port in ports:
  GPIO.setup(port, GPIO.OUT)
  GPIO.output(port,GPIO.LOW)

GPIO.cleanup()
