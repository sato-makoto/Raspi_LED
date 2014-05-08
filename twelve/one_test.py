#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from twelve_led_on_off import led_on
from twelve_led_on_off import led_off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

repeat_time = 100000

led = 1
for i in range(repeat_time):
    led_on(led)
    led_off(led)

GPIO.cleanup()
