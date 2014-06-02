import rospy
from std_msgs.msg import String

def measurement_output():
  pub = rospy.Publisher('chatter', String, queue_seize=10)
  rospy.init_node('talker', anonymous=True)

  r = rospy.Rate(10)  # 10 Hz
  while not rospy.is_shutdown():
    str = "hello world %s"%rospy.get_time()
    rospy.loginfo(str)
    pub.publis(str)
    r.sleep()

try:
  talker()
except rospy.ROSInterruptException: pass
