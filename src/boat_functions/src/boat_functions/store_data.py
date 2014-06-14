#!/usr/bin/env python
# this line is needed so the execution happens in python environment

import rospy
from std_msgs.msg import Header

def init_empty_1d(length, name):
""" init_empty_1d initialises empty list
    for storing 1d values
    it can keep (length) values
    """
    template = {
    'name': name,
    'value': [0 for x in range(lenght)
    }
    return template

def init_empty_3d(length, name):
""" init_empty_3d initialises empty list
    for storing 3d values
    it can keep (length) values
    """
    template = {
    'name': name,
    'x': [0 for x in range(length)],
    'y': [0 for x in range(length)],
    'z': [0 for x in range(length)]
    }


def store3dROS(data, storage):
""" insert new header + three directional measurements
    in the handed over storage list, remove oldest value
    """
    storage['header'].insert(0, data.header)
    storage['header'].pop()
    storage['x'].insert(0, data.x_value)
    storage['x'].pop()
    storage['y'].insert(0, data.y_value)
    storage['y'].pop()
    storage['z'].insert(0, data.z_value)
    storage['z_value'].pop()
    rospy.loginfo(
    'add x_value ' + str(storage['x_value'][0]) + 
    ' y_value ' + str(storage['y_value'][0]) +
    ' z_value ' + str(storage['z_value'][0]) +
    ' to ' + storage['name'])
    rospy.logdebug(storage)

def store1dROS(data, storage):
""" insert new header + 1d  measurement
    in the handed over storage list, remove oldest value
    """
    storage['header'].insert(0, data.header)
    storage['header'].pop()
    storage['value'].insert(0, data.value)
    storage['value'].pop()
    rospy.loginfo(
    'add value ' + str(storage['value'][0]) + 
    ' to ' + storage['name'])
    rospy.logdebug(storage)

