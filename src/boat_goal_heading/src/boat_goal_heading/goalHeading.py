from sensor_msgs.msg import NavSatFix
from LatLon import *

def calc_heading(position, waypoint):
    pos = LatLon(Latitude(position.latitude), Longitude(position.longitude))
    wp = LatLon(Latitude(waypoint[0]), Longitude(waypoint[1]))
    # get angle between pos and wp
    angle = pos.heading_initial(wp)

    # check if these directions are good for sailing
    if angle < 45:
        angle = 45
    elif angle > 135:
        angle = 135
    return angle

