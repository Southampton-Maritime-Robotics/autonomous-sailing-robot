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
air = [0 for x in range(history_length)]
accelerometer = [["header", 0, 0, 0] for x in range(history_length)]

def accelerometerPrint(data):
    rospy.loginfo(rospy.get_caller_id()+"""
    I heard x acceleration is %i, 
    y acceleration is %i, 
    z acceleration is %i;
    Header: %s""", data.x_value, data.y_value, data.z_value, data.header)
     
def airPressurePrint(data):
    rospy.loginfo(rospy.get_caller_id()+"""
    I heard air pressure is %i""",
    data.data)

def storeAirPressure(data):
    airPressure.insert(0,data.data)
    airPressure.pop()
    print(airPressure)

def storeIntROS(data, storage):
    """ insert new Int value received from ROS in
    the storage list, remove oldest value
    """
    storage.insert(0,data.data)
    storage.pop()
    print(storage)

def store3dROS(data, storage):
    """ insert new header + three directional measurements
    in the handed over storage list, remove oldest value
    """
    storage.insert(0,[data.header, data.x_value, data.y_value, data.z_value])
    storage.pop()
    print(storage)

def listener():
    rospy.init_node('listener', anonymous=True)
    #rospy.Subscriber("AirPressure", Int64, airPressurePrint)
    #rospy.Subscriber("Accelerometer", measurements, accelerometerPrint)
    rospy.Subscriber("AirPressure", Int64, storeAirPressure)
    rospy.Subscriber("AirPressure", Int64, storeIntROS, air)
    rospy.Subscriber("Accelerometer", measurements, store3dROS, accelerometer)
    rospy.spin()
                                                    

if __name__ == '__main__':
    listener()
