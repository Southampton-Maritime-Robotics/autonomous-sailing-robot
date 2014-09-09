from sensor_msgs.msg import NavSatFix
from LatLon import *

def calc_heading(position, waypoint):
    pos = LatLon(Latitude(position.latitude), Longitude(position.longitude))
    wp = LatLon(Latitude(waypoint[0]), Longitude(waypoint[1]))
    angle = pos.heading_initial(wp)
    return angle

