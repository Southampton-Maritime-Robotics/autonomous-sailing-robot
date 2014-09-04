"""
test PWM

"""
from bbio import *

analogWrite(PWM1A, 0)
#analogWrite(PWM1B, 0)
# results in IndexError: list index out of range
analogWrite(PWM2A, 0)
#analogWrite(PWM2B, 0)
# results in IndexError: list index out of range
