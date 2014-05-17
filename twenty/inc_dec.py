#!/usr/bin/env python
# -*- coding: utf-8 -*-

# check GPIO 28 and 31
# when press red or green button
# led on after or before one

import RPi.GPIO as GPIO
import twenty_on_off as TW
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

first_led = 0
last_led = 19
led_num = 20

def input_check(port):
  button = GPIO.input(port)
  return (button)

def led_number(led):
  if led < first_led:
    led +=  led_num
  if led > last_led:
    led -= led_num
  TW.led_on(led)
  return led

ports = [28, 30, 31]
GPIO.setup(ports[0], GPIO.IN)
GPIO.setup(ports[1], GPIO.OUT)
GPIO.setup(ports[2], GPIO.IN)
GPIO.output(ports[1], GPIO.HIGH)
led = first_led
led_number(led)

while True:
  for port in ports[::2]:
    check = input_check(port)
    if check == False:
      if port == ports[0]:
        TW.led_off(led)
        led += 1
        led = led_number(led)
      elif port == ports[2]:
        TW.led_off(led)
        led -= 1
        led = led_number(led)
      while check == False:
        check = input_check(port)
