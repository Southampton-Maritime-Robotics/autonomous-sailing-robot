#!/usr/bin/env python
# this line is needed so the execution happens in python environment

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Header
from boat_imu.msg import measurements

# number of remembered values
history_length = 5
""" Air pressure history
 AirPressure[0] newest """
airPressure = [0 for x in range(history_length)]
accelerometer = [["header", 0, 0, 0] for x in range(history_length)]
magnetometer = [["header", 0, 0, 0] for x in range(history_length)]
gyroscope = [["header", 0, 0, 0] for x in range(history_length)]
# TODO make this a dictionary, that contains: name, header, values
# maybe even dimension?
print('test')
#rospy.loginfo("some text")
print('test')

def storeIntROS(data, storage):
    """ insert new Int value received from ROS in
    the storage list, remove oldest value
    """
    storage.insert(0,data.data)
    storage.pop()
    rospy.logdebug("add value" + str(storage[0]))
    rospy.logdebug(storage)

def store3dROS(data, storage):
    """ insert new header + three directional measurements
    in the handed over storage list, remove oldest value
    """
    storage.insert(0,[data.header, data.x_value, data.y_value, data.z_value])
    storage.pop()
    rospy.logdebug("add value" + str(storage[0]))
    rospy.logdebug(storage)


def imu_listener():
    rospy.init_node('listener', anonymous=True)
    rospy.loginfo('ros imu listener started')
    rospy.Subscriber("AirPressure", Int64, storeIntROS, airPressure)
    rospy.Subscriber("Accelerometer", measurements, store3dROS, accelerometer)
    rospy.Subscriber("Magnetometer", measurements, store3dROS, magnetometer)
    rospy.Subscriber("Gyroscope", measurements, store3dROS, magnetometer)
    rospy.spin()
                                                    

if __name__ == '__main__':
    imu_listener()

