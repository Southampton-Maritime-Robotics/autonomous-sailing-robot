#!/usr/bin/env python
# this line is needed so the execution happens in python environment

import rospy
from std_msgs.msg import String
from boat_imu.msg import measurements

def talker():
    pubString = rospy.Publisher('chatter', String, queue_size=10)
    pubAcc = rospy.Publisher('Accelerometer', measurements, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str = "hello world %s"%rospy.get_time()
        #rospy.loginfo(str)
        pubString.publish(str)
        int = 1
        #rospy.loginfo(int)
        pubString.publish(int)
        test_measurement = measurements(1,2,3)
        #rospy.loginfo(test_measurement)
        pubAcc.publish(test_measurement)

        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
