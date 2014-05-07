"""
Function set for LED functions
currently available pins:
GPIO1_13 (green, LED 3)
GPIO1_12 (red, LED 3)

GPIO1_14 (green, LED 4)
GPIO0_26 (red, LED 4)
"""

import Adafruit_BBIO.GPIO as GPIO
import time
LED3_RED = "GPIO1_12"
LED3_GREEN = "GPIO1_13"
LED4_RED = "GPIO0_26"
LED4_GREEN = "GPIO1_14"


#TODO is this allways run when this set
# of functions is imported?
GPIO.setup(LED3_RED, GPIO.OUT)
GPIO.setup(LED3_GREEN, GPIO.OUT)
GPIO.setup(LED4_RED, GPIO.OUT)
GPIO.setup(LED4_GREEN, GPIO.OUT)

#def blink(pin):
#    #TODO can this just toggle between HIGH and LOW every time it is called??

def led_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def led_off(pin):
    GPIO.output(pin, GPIO.LOW)

def blinktest():
	while True:
	    led_on(LED3_RED)
	    time.sleep(1)
	    led_off(LED3_RED)
	    led_on(LED3_GREEN)
	    time.sleep(1)
	    led_off(LED3_GREEN)
	    time.sleep(1)

if __name__ == "__main__":
    blinktest()
