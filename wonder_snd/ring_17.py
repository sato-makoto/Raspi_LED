#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 
import time
import RPi.GPIO as GPIO

port = 17
dulate_sec = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)

GPIO.output(port,GPIO.HIGH)
time.sleep(dulate_sec)
GPIO.cleanup()
