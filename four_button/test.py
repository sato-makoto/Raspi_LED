#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Check from GPIO 28 to 31
# when GPIO is False
# print messages of button 
# pressed

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def input_check(port):
  button = GPIO.input(port)
  return (button, port)

esc = [31, 37, 33, 30]
seq_begin = '\033[1;'
seq_end = '\033[00m'

ports = [28, 29, 30, 31]
for port in ports:
  GPIO.setup(port, GPIO.IN)

while True:
  for port in ports:
    check = input_check(port)
    if check[0] == False:
      if port == ports[0]:
        print '{0}{1}m赤い釦{2}が押されました' . \
          format(seq_begin, esc[0], seq_end)
      elif port == ports[1]:
        print '{0}{1}m白い釦{2}が押されました' . \
          format(seq_begin, esc[1], seq_end)
      elif port == ports[2]:
        print '{0}{1}m黄の釦{2}が押されました' . \
	  format(seq_begin, esc[2], seq_end)
      elif port == ports[3]:
        print '{0}{1}m灰の釦{2}が押されました' . \
	  format(seq_begin, esc[3], seq_end)
      while check[0] == False:
        check = input_check(port)
