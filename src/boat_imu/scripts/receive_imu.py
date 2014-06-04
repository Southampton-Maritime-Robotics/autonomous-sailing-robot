import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Header
from boat_imu.msg import measurements

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
        
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("AirPressure", Int64, callback)
    rospy.spin()
                                                    
if __name__ == '__main__':
    listener()
