#!/usr/bin/env python
# this line is needed so the execution happens in python environment

import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from boat_imu.msg import measurements

def talker():
    pubString = rospy.Publisher('chatter', String, queue_size=10)
    pubAcc = rospy.Publisher('Accelerometer', measurements, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    h = Header()
    while not rospy.is_shutdown():
        # generate header
        #h = Header()
        h.stamp = rospy.Time.now()
 
        str = "hello world %s"%rospy.get_time()

        #rospy.loginfo(str)
        pubString.publish(str)
        int = 1
        #rospy.loginfo(int)
        pubString.publish(int)
        test_measurement = measurements(h,1,2,3)
        rospy.loginfo(test_measurement)
        # in the loginfo the seq number stays 0
        # the actual messages contain increasing numbers
        # as set by the publisher

        pubAcc.publish(test_measurement)

        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
