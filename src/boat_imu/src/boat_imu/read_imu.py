"""
Read sensor Values from 9DOF IMU
If there is no 9DOF IMU
(not connected, running on a different machine for testing, ...)
the simulation data is used instead.
The green LED is on if sensor values are used,
the red LED indicates that simulation values are used.
"""

import Adafruit_BBIO.GPIO as GPIO
# select pin for imu LED
GPIO.setup("P8_10", GPIO.OUT) #!!! which pin?

# Try reading the sensor
# set LED GREEN


# Read simulation value instead
# set LED RED


# set LED
