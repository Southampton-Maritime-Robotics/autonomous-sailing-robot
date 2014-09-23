"""
Simulator, using logs from the autonomous sailing robot to analyse performance
"""
import pygame
from pygame.locals import *
from os import path
from  math import *

from boat_oil_sensor.testvalues import simulated_oil
#from testvalues import simulated_oil

WATER_COLOUR = pygame.Color(152, 242, 255)
OIL_COLOUR = pygame.Color(28, 28, 16)

PIXELS_PER_METER = 50
MARGIN = 1

FONT_SIZE = 20

# All below _should_ be executed on import?
xMin = min(x for x,y in simulated_oil)
xMax = max(x for x,y in simulated_oil)
yMin = min(y for x,y in simulated_oil)
yMax = max(y for x,y in simulated_oil)

area_width = xMax - xMin + 2*MARGIN
area_height = yMax - yMin + 2*MARGIN

pygame.init()

text_font = pygame.font.SysFont("Arial", FONT_SIZE)
pygame.display.set_caption('Autonomous Sailing Robot - Simulator')

"""
Plot water area of interest
"""
area_size = (int((area_width) * PIXELS_PER_METER), int((area_height) * PIXELS_PER_METER))
DISPLAYSURF = pygame.display.set_mode(area_size)
DISPLAYSURF.fill(WATER_COLOUR)
#water = pygame.Rect(0,0,area_size[0], area_size[1])

#while True: # main game loop
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

        pygame.display.update()


def to_pixel_coord(world_coord):

    xMin = min(x for x,y in simulated_oil)
    xMax = max(x for x,y in simulated_oil)
    yMin = min(y for x,y in simulated_oil)
    yMax = max(y for x,y in simulated_oil)

    offset_x = xMin - MARGIN
    offset_y = yMin - MARGIN
    x, y = world_coord
    x, y = ((x - offset_x) * PIXELS_PER_METER , (y - offset_y) * PIXELS_PER_METER )
    return (int(x), int(y))



"""
Plot simulated oil spill

The oil spill is simulated by the boat_oil_sensor node (for now),
so the goal oil spill result can be plotted beforehand.
"""
oil_coord = []
for i in simulated_oil:
    oil_coord.append(to_pixel_coord(i))
pygame.draw.polygon(DISPLAYSURF, OIL_COLOUR, oil_coord)
mainPlotting()




"""
Plot wind direction, speed

The wind direction and speed are currently determined
before the experiment starts.

TODO: expand this to use wind logs, so it can change for
different wind directions once a sensor is used

"""
def plotWind(WindDirection):
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
    mainPlotting()
    print("plotted")


"""
Plot boat position
"""
def plotPosition(GPS):
    x = int(GPS.latitude * PIXELS_PER_METER)
    y = int(GPS.longitude * PIXELS_PER_METER)
    print(x)
    print(y)
    pygame.draw.circle(DISPLAYSURF, (0,200,0), (x, y), 5, 0)
    mainPlotting()

"""
Plot oil sensor result
"""

"""
Plot point of sail, boat direction
"""

"""
Plot boat speed
"""
