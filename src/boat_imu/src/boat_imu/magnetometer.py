"""
read and evaluate the i2c magnetometer
HMC5883L
calibration:
http://www.timzaman.com/?p=994
"""


from bbio import *
def  transformReadable(raw_data):
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

Wire2.begin()
while(1):
    Wire2.write(0x1e,2,1)
    # detailed magnetometer read, incl. mode, status
    raw_data = Wire2.read(0x1e, 0, 10)
    print(raw_data)
    mag = transformReadable(raw_data)
    print("x-value: %d" %mag[0]),
    print("y-value: %d" %mag[1]),
    print("z-value: %d" %mag[2])

