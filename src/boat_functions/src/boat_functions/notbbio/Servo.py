"""
Set of test functions
so BeagleBone specific GPIO
functions can be tested

For obvious reasons these values
are ONLY for testing!

TODO:
Expand to use test values instead of set values
"""


def Servo(someChar):
    print("simulated Servo")
    return 23

def attach(self, pin):
    print("Attached simulated servo to " + char(pin))

def write(self, angle):
    print("Set servo to "+ char(angle))

