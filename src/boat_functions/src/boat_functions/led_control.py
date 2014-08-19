import Adafruit_BBIO.GPIO as GPIO
import time
LED_RED_1 = "P8_4"
while True:
    GPIO.setup(LED_RED_1, GPIO.OUT)
    GPIO.setup(LED_RED_1, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_RED_1, GPIO.LOW)
    time.sleep(0.5)

