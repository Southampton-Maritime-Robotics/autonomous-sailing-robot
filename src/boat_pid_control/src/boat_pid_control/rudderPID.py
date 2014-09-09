"""
PID control for the sailing robot
controling sail position
based on goal sail direction

Inputs: 
- current heading
- goal heading

Output:
- Change in motor position/motor position

TODO:
consider tack and jibe
"""

import rospy


PROPORTIONAL_GAIN = 0.1
INTEGRAL_GAIN = 0
DERIVATIVE_GAIN = 0


currentHeading = 23
goalHeading = 35

def get_pid(currentHeading, goalHeading):
    # with new ROS input for goal or current heading

    # Error calculation for angular error!
    error = currentHeading - goalHeading


    p = error * PROPORTIONAL_GAIN
    i = 0
    d = 0

    correction = p + i + d
    rudder_position = 2
    #translate correction to servo change ...

return rudder_position
