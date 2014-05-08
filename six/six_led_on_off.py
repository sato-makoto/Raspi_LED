import time
import RPi.GPIO as GPIO

# light one LED
# GPIO: [OUT_HIGH_PORT,
#        OUT_LOW_PORT, 
#        IN_PORT]

#LED 0 on: [30, 29, 28]
#LED 1 on: [29, 30, 28]
#LED 2 on: [30, 28, 29] 
#LED 3 on: [28, 30, 29]
#LED 4 on: [28, 29, 30]
#LED 5 on: [29, 28, 30]


leds = [[30, 29, 28],
        [29, 30, 28],
        [30, 28, 29],
        [28, 30, 29],
        [28, 29, 30],
        [29, 28, 30]]

def led_on(port):
  l_port, out_port, in_port = leds[port]
  GPIO.setup(in_port, GPIO.IN)
  GPIO.setup(out_port, GPIO.OUT)
  GPIO.setup(l_port, GPIO.OUT)
  GPIO.output(l_port,GPIO.HIGH)

def led_off(port):
  l_port, out_port, in_port = leds[port]
  GPIO.output(l_port,GPIO.LOW)

def led_clean():
  for port in leds[0]:
    GPIO.setup(port, GPIO.OUT)
    GPIO.setup(port, GPIO.LOW)
    GPIO.setup(port, GPIO.IN)
