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
# empty history to initialise storage lists
empty_history = [0 for x in range(history_length)]
empty_header_history = ["header" for x in range(history_length)]


airPressure = {
'name': 'AirPressure', 
'value': list(empty_history)}


accelerometer = {
'name': 'Accelerometer',
'header': map(str, list(empty_history)),
'x_value': list(empty_history),
'y_value': list(empty_history),
'z_value': list(empty_history)
}

magnetometer = {
'name': 'Magnetometer',
'header': map(str, list(empty_history)),
'x_value': list(empty_history),
'y_value': list(empty_history),
'z_value': list(empty_history)
}

gyroscope = {
'name': 'Gyroscope',
'header': map(str, list(empty_history)),
'x_value': list(empty_history),
'y_value': list(empty_history),
'z_value': list(empty_history)
}

def storeIntROS(data, storage):
    """ insert new Int value received from ROS in
    the storage list, remove oldest value
    """
    storage['value'].insert(0,data.data)
    storage['value'].pop()
    rospy.loginfo(
    "add value " + str(storage['value'][0]) + ' to ' + storage['name'])
    rospy.logdebug(storage)

def store3dROS(data, storage):
    """ insert new header + three directional measurements
    in the handed over storage list, remove oldest value
    """
    storage['header'].insert(0, data.header)
    storage['header'].pop()
    storage['x_value'].insert(0, data.x_value)
    storage['x_value'].pop()
    storage['y_value'].insert(0, data.y_value)
    storage['y_value'].pop()
    storage['z_value'].insert(0, data.z_value)
    storage['z_value'].pop()

    rospy.loginfo(
    'add x_value ' + str(storage['x_value'][0]) + 
    ' y_value ' + str(storage['y_value'][0]) +
    ' z_value ' + str(storage['z_value'][0]) +
    ' to ' + storage['name'])
    rospy.logdebug(storage)
    rospy.logdebug(accelerometer)
    rospy.logdebug('!!!!!!!!!!')

def imu_listener():
    rospy.init_node('listener', anonymous=True)
    rospy.loginfo('ros imu listener started')
    rospy.Subscriber("AirPressure", Int64, storeIntROS, airPressure)
    rospy.Subscriber(accelerometer['name'], measurements, store3dROS, accelerometer)
    rospy.Subscriber("Magnetometer", measurements, store3dROS, magnetometer)
    rospy.Subscriber("Gyroscope", measurements, store3dROS, gyroscope)
    rospy.spin()
                                                    

if __name__ == '__main__':
    imu_listener()
