import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Header
from boat_imu.msg import measurements

history_length = 5
airPressure = [0 for x in range(history_length)]

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

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("AirPressure", Int64, airPressurePrint)
    rospy.Subscriber("Accelerometer", measurements, accelerometerPrint)
    rospy.Subscriber("AirPressure", Int64, storeAirPressure)
    rospy.spin()
                                                    

if __name__ == '__main__':
    listener()
