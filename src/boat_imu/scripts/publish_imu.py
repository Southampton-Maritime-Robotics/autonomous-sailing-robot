#!/usr/bin/env python
# this line is needed so the execution happens in python environment


# script to publish 9DOF IMU data

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Header
from boat_imu.msg import measurements

def talker():
    pubPressure = rospy.Publisher('AirPressure', Int64, queue_size=10)
    pubAcc = rospy.Publisher('Accelerometer', measurements, queue_size=10)
    pubGyro = rospy.Publisher('Gyroscope', measurements, queue_size=10)
    pubMagnet = rospy.Publisher('Magnetometer', measurements, queue_size=10)
    

    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    h = Header()
    while not rospy.is_shutdown():
        # update header time
        h.stamp = rospy.Time.now()

# TODO: int or float measurements??
        air_p = 1
        acc_x = 1
        acc_y = 2
        acc_z = 3
        gyro_x = 11
        gyro_y = 12
        gyro_z = 13
        magnet_x = 21
        magnet_y = 22
        magnet_z = 23

        rospy.loginfo(air_p)
        pubPressure.publish(air_p)

        # assemble, publish measurement messages
        acc_msg = measurements(h,acc_x,acc_y,acc_z)
        rospy.loginfo(acc_msg)
        # in the loginfo the seq number stays 0
        # the actual messages contain increasing numbers
        # as set by the publisher
        pubAcc.publish(acc_msg)

        gyro_msg = measurements(h,gyro_x,gyro_y,gyro_z)
        rospy.loginfo(gyro_msg)
        pubGyro.publish(gyro_msg)

        magnet_msg = measurements(h,magnet_x,magnet_y,magnet_z)
        rospy.loginfo(magnet_msg)
        pubMagnet.publish(magnet_msg)



        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
