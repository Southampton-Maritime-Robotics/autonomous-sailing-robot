"""
Set of test functions
so BeagleBone specific GPIO
functions can be tested

For obvious reasons these values
are ONLY for testing!

TODO:
Expand to use test values instead of set values
"""

def begin():
    print("WARNING, not using actual GPIO")

def write(address, a, b):
    #print("WARNING, not actual GPIO")
    pass

def read(address, start, lenght):
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
