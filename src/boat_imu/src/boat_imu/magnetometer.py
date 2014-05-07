"""
read and evaluate the i2c magnetometer
HMC5883L
calibration:
http://www.timzaman.com/?p=994
"""

import time
import math

# try to import BBB specific libraries
try:
    from bbio import *
except:
    from boat_functions.notbbio import *
    print("Using BBIO test library!")
    print("WARNING! No useful values!")
    pass


from os.path import expanduser

try:
    home = expanduser("~")
    f = open(home + '/boat_data_compass', 'r')
    OFFSET = [0, 0, 0]
    OFFSET[0] = int(f.readline())
    OFFSET[1] = int(f.readline())
    OFFSET[2] = int(f.readline())
    f.close()
except:
    print("WARNING: No calibration file found")
    OFFSET = [0,0,0]

AVERAGE_TIME = 1

Wire2.begin()

def  transform_readable(raw_data):
    """ 
    transforms the values directly from IMU into readable values
    values go approximately 0 -> + 1000 -> 0 -> - 1000 -> 0
    """

    mag = [0, 0, 0]
    for i in range(3):
        if (raw_data[2*i + 3] < 0x10):
            mag[i] = raw_data[2*i + 3]*0x100 + raw_data[2*i + 1 + 3]
        else:
            mag[i] = -(0x10000 - (raw_data[2*i + 3]*0x100 + raw_data[2*i + 1 + 3])) 
    # get the magnetometer measurements in x, y, z order
    storage = mag[1]
    mag[1] = mag[2]
    mag[2] = storage
    return mag

def get_offset(sample_time):
    """
    Find simple offsett values.
    During the sample time of this function 
    the BBB with the magnetometer on should be rotated
    along all axis.

    sample_time is in seconds
    """
    start = time.clock()
    mag_samples = []
    mag_max = [0,0,0]
    mag_min = [0,0,0]
    offset = [0,0,0]

    while (time.clock() - start) < sample_time:
        raw_data = get_raw_mag()
        mag_samples.append(transform_readable(raw_data))
        # blink leds to signify timespan

    while mag_samples != []:
        a = mag_samples.pop()
        # find maximum, minimum Values
        for i in range(3):
            if (a[i] > mag_max[i]):
                mag_max[i] = a[i]
            if (a[i] < mag_max[i]):
                mag_min[i] = a[i]
        #print(mag_max)
        #print(mag_min)

        # calculate offset from Extrema
        for i in range(3):
            offset[i] = (mag_max[i] + mag_min[i])/2
    return offset

def get_raw_mag():
    """
    read raw data via i2c
    from HMC5883L on address 0x1e
    """
    Wire2.write(0x1e,2,1)
    # detailed magnetometer read, incl. mode, status
    raw_data = Wire2.read(0x1e, 0, 10)
    return raw_data

def subtract_offset(value):
    for i in range(3):
        value[i] = value[i] - OFFSET[i]
    return value

def calc_angle(x, y):
    compass_angle = math.atan2(-x, -y)
    compass_angle = math.degrees(compass_angle + 3.1415)
    return compass_angle

def read_magnetometer():
    """
    full function reading magnetometer
    """
    compass = get_raw_mag()
    compass = transform_readable(compass)
    compass = subtract_offset(compass)
    return compass

def average_value(av_time):
    a = []
    av_value = [0, 0, 0]
    start = time.time()
    while(time.time() - start) < av_time:
        a.append(read_magnetometer())
        time.sleep(0.1)
    for i in range(len(a)):
        for k in range(3):
            av_value[k] += a[i][k]

    for k in range(3):
        av_value[k] = av_value[k] / len(a)

    return av_value

def get_mag_angle(av_time):
    compass = average_value(av_time)
    compass_angle = calc_angle(compass[2], compass[1])
    return compass_angle

if __name__ == '__main__':
    lala = get_offset(0.2)
    print(lala)
    while(1):
        raw_data = get_raw_mag()
        mag = transform_readable(raw_data)
        print("x-value: %d" %mag[0]),
        print("y-value: %d" %mag[1]),
        print("z-value: %d" %mag[2])
        print(get_mag_angle(AVERAGE_TIME))
