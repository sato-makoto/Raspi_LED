import RPi.GPIO as GPIO
ports = [17, 18, 27, 22, 23, 24, 25, 4]
right = 28
left = 29

a,b,c,d,e,f,g,h = ports
led_array = [ 
 [a, b, e, f, g, h], 
 [f, g], 
 [a, d, e, g, h], 
 [d, e, f, g, h], 
 [b, d, f, g], 
 [b, d, e, f, h], 
 [a, b, d, e, f, h], 
 [b, f, g, h], 
 [a, b, d, e, f, g, h], 
 [b, d, e, f, g, h], 
]

def right_left(num):
  if num < 10:
    return num, 0
  else:
    numstr = str(num)
    rnum, lnum = int(numstr[1]), int(numstr[0])
    return rnum, lnum

def led_on(num, rf):
  for x in led_array[num]:
    GPIO.setup(x, GPIO.OUT)
  GPIO.setup(rf, GPIO.OUT)
  GPIO.output(rf, GPIO.HIGH)

def led_off(num, rf):
  for x in led_array[num]:
    GPIO.setup(x, GPIO.OUT)
  GPIO.output(rf, GPIO.LOW)
  GPIO.setup(rf, GPIO.IN)
