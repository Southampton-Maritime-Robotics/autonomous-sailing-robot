"""
Simulator, using logs from the autonomous sailing robot to analyse performance
"""
import pygame
from pygame.locals import *
from os import path
from  math import *
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Header
from std_msgs.msg import Int64
from sensor_msgs.msg import NavSatFix

# import test values
from boat_oil_sensor.testvalues import simulated_oil
#from testvalues import simulated_oil

WATER_COLOUR = pygame.Color(152, 242, 255)
OIL_COLOUR = pygame.Color(28, 28, 16)

#TODO: calculate these measurements from
# assumed screen hight, width
PIXELS_PER_METER = 3
MARGIN = 20
GPS = 100000 # factor to make GPS coordinates handle-able
YSTRETCH = 1.5

FONT_SIZE = 20

# All below _should_ be executed on import?
yMin = min(x*GPS for x,y in simulated_oil)
yMax = max(x*GPS for x,y in simulated_oil)
xMin = min(y*GPS for x,y in simulated_oil)
xMax = max(y*GPS for x,y in simulated_oil)

area_width = xMax - xMin + 2*MARGIN
area_height = yMax - yMin + 2*MARGIN

pygame.init()

text_font = pygame.font.SysFont("Arial", FONT_SIZE)
pygame.display.set_caption('Autonomous Sailing Robot - Simulator')

area_size = (int((area_width) * PIXELS_PER_METER), int((area_height) * PIXELS_PER_METER* YSTRETCH))
DISPLAYSURF = pygame.display.set_mode(area_size)

def to_pixel_coord(world_coord):

    yMin = min(x*GPS for x,y in simulated_oil)
    yMax = max(x*GPS for x,y in simulated_oil)
    xMin = min(y*GPS for x,y in simulated_oil)
    xMax = max(y*GPS for x,y in simulated_oil)

    offset_x = xMin - MARGIN
    offset_y = yMin - MARGIN
    x, y = world_coord
    x, y = ((x - offset_x) * PIXELS_PER_METER , 
    (yMax + MARGIN - y ) * PIXELS_PER_METER * YSTRETCH)# negative sign, streched

    return (int(x), int(y))

def plotBackground():
    """
    Plot water area of interest
    """
    DISPLAYSURF.fill(WATER_COLOUR)

    """
    Plot simulated oil spill

    The oil spill is simulated by the boat_oil_sensor node (for now),
    so the goal oil spill result can be plotted beforehand.
    """
    
    oil_coord = []
    for x,y in simulated_oil:
        oil_coord.append(to_pixel_coord((x*GPS,y*GPS)))
    pygame.draw.polygon(DISPLAYSURF, OIL_COLOUR, oil_coord)
    



"""
Plot wind direction, speed

The wind direction and speed are currently determined
before the experiment starts.

TODO: expand this to use wind logs, so it can change for
different wind directions once a sensor is used

"""

def plotWind(WindDirection):
    pass
    """
    wind_dir_char = str(WindDirection.data)
    wind_info = text_font.render("Wind Direction: " + wind_dir_char, 1, OIL_COLOUR)
    bottom_left= area_size[1] - 2*FONT_SIZE
    DISPLAYSURF.blit(wind_info, (0,bottom_left))
    offset_x = (sin(radians(WindDirection.data))) * 50
    offset_y = (cos(radians(WindDirection.data))) * 50
    pygame.draw.lines(DISPLAYSURF, (0,0,0), False, [
    (20,bottom_left), (20 + offset_x,bottom_left-offset_y)], 2)
    pygame.draw.lines(DISPLAYSURF, (200,0,0), False, [
    (20 + offset_x, bottom_left-offset_y),
    (20 + offset_x*0.9, bottom_left-offset_y*0.9)], 3)
    pygame.display.flip()
    """

"""
Log boat position
"""
gps_log = []
def store_gps(wp):
    global gps_log
    current_value = ((wp.longitude)*GPS,(wp.latitude)*GPS)
    #current_value = (wp.latitude, wp.longitude)
    current_value = to_pixel_coord(current_value)
    gps_log.append(current_value)
    print('gotgps')
    mainPlotting()
    print('plotted')
    #print(gps_log)

"""
plot log of boat positions
"""
def plotBoatHistory():
    global gps_log
    if len(gps_log)>3:
        for a in gps_log: 
            pygame.draw.circle(DISPLAYSURF, (0,50,100), a, 3, 0)
    print("draw log")

"""
Plot boat position
"""
def plotBoat():
    global gps_log
    loglen = len(gps_log)
    coord = gps_log[loglen-1]
    pygame.draw.circle(DISPLAYSURF, (0,200,0), coord, 5, 0)

"""
Plot oil sensor result
"""

"""
Plot point of sail, boat direction
"""

"""
Plot boat speed
"""

#while True: # main game loop
# this is run every time something is received from an node (== new data)
def mainPlotting():
    for event in pygame.event.get():
        # TODO: is the interrupt really needed once this is in a ros package?
        #  cover two ways to quit: ESC key
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        # cover two ways to quit: x-button on window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    plotBackground()
    print("about to plot")
    plotBoatHistory()
    plotBoat()
    pygame.display.flip()
    #pygame.display.update()


