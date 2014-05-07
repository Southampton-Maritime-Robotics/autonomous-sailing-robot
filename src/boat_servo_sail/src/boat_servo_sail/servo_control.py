"""
test PWM

"""
from bbio import *
from Servo import *
import time


servo1 = Servo(PWM1A)
servo2 = Servo(PWM2A)
servo1.write(20)
servo2.write(20)
time.sleep(2)
servo1.write(0)
servo2.write(0)
