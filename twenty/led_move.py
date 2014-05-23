#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Check from GPIO 28 to 31
# when GPIO is False
# print messages of button 
# pressed

import RPi.GPIO as GPIO
from sys import argv
import twenty_on_off as TW

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

cont_ports = [28, 29, 30, 31]
for port in cont_ports:
  GPIO.setup(port, GPIO.IN)
ledports = TW.light_num

led = 0
TW.led_on(led)

while True:
  for port in cont_ports:
    check = TW.input_check(port)
    if check == False:
      if port == cont_ports[0]:
         TW.led_off(led)
	 led = TW.move_right(led)
         TW.led_on(led)
      elif port == cont_ports[1]:
         TW.led_off(led)
	 led = TW.move_lower(led)
         TW.led_on(led)
      elif port == cont_ports[2]:
         TW.led_off(led)
	 led = TW.move_left(led)
         TW.led_on(led)
      elif port == cont_ports[3]:
         TW.led_off(led)
	 led = TW.move_upper(led)
         TW.led_on(led)
      while check == False:
        check = TW.input_check(port)
