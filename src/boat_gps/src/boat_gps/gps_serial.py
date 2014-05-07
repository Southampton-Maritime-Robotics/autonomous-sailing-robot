# serial_echo.py - Alexander Hiam - 4/15/12
#
# Prints all incoming data on Serial2 and echos it back.
#
# Serial2 TX = pin 21 on P9 header
# Serial2 RX = pin 22 on P9 header
#
# This example is in the public domain
from bbio import *

def setup():
    # Start Serial2 at 9600 baud:
    Serial4.begin(9600)

   
setup()
while(1):
    a = Serial4.ser_port.readline()
    print a
