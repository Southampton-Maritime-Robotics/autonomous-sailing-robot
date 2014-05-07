"""
read and evaluate the i2c magnetometer
HMC5883L
calibration:
http://www.timzaman.com/?p=994
"""


from bbio import *

Wire2.begin()
while(1):
    Wire2.write(0x1e,2,1)
    # detailed magnetometer read, incl. mode, status
    raw_data = Wire2.read(0x1e, 0, 10)
    raw_data = Wire2.read(0x1e, 3, 6)
    print(raw_data)

    mag_X = raw_data[0]*0x100 + raw_data[1]
    mag_Z = raw_data[2]*0x100 + raw_data[3]
    mag_Y = raw_data[4]*0x100 + raw_data[5]
    print("x-value: %d" %mag_X),
    print("y-value: %d" %mag_Y),
    print("z-value: %d" %mag_Z)

"""
current calculation doesn't consider the sign of the MSB...
"""
