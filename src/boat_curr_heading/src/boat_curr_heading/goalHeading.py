from sensor_msgs.msg import NavSatFix
from LatLon import *

def calc_heading(position, waypoint):
    print position.latitude
    print position.longitude
    angle = 23
    print angle

    pos = LatLon(Latitude(position.latitude), Longitude(position.longitude))
    wp = LatLon(Latitude(waypoint[0]), Longitude(waypoint[1]))
    angle = pos.heading_initial(wp)
    print(angle)
    return angle

