autonomous-sailing-robot
========================
ROS based firmware for an Autonomous Sailing Robot (ASR).
The ASR is implemented using a BeagleBone Black as the main control board.
The sailing boat is an RC Laser boat, but any boat with two servos,
one for rudder control and one for sheet control should work with this setup.

Sensors:
- GPS
- 9 DOF imu
- Oil sensor (always simulated)
- Wind sensor (set to constant value)
