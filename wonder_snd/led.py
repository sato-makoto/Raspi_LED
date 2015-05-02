#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 
from time import  sleep

from port_pin_on_off import on, off, clean

"""
PORT  JP
24    1
17    2
18    3
22    5
23    6
27    4

"""
try:
  pin = int(argv[1])
  sleeptime = int(argv[2])
except:
  print "no JP Nonber"
  exit(1)


print \
  '{} pin by {} seconds.'\
    .format(pin, sleeptime)

on(pin)
sleep(sleeptime)
off(pin)
clean()
