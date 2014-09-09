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
from pid_controller_class import PID

PROPORTIONAL_GAIN = 0.1
INTEGRAL_GAIN = 0
DERIVATIVE_GAIN = 0
INTEGRAL_LIMIT = 1

controller = PID(PROPORTIONAL_GAIN, INTEGRAL_GAIN, DERIVATIVE_GAIN, INTEGRAL_LIMIT, -INTEGRAL_LIMIT)

currentHeading = 23
goalHeading = 35

def angle_difference(currentHeading, goalHeading):
    difference = goalHeading - currentHeading
    if difference < 0:
        difference += 360
    elif difference > 360:
        difference -= 360
    return difference

def get_pid(currentHeading, goalHeading):
    # with new ROS input for goal or current heading

    # TODO Error calculation for angular error!
    error = angle_difference(currentHeading,goalHeading)
    correction = controller.update_PID(error)
    rudder_position = 2
    #translate correction to servo change ...

    return rudder_position
