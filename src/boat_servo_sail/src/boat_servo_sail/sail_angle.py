import bisect

def calculate_angle_boat_wind(boat_compass, wind_direction):
    wind_dir = wind_direction
    angle = abs(boat_compass - wind_dir)
    if angle > 180:
        angle = 360 - angle
    return angle


def assign_length(diff_wind_boat):
    angles = [
        (45, 1), #downwind
        (50, 0.95),
        (60, 0.9),
        (70, 0.85),
        (80, 0.8),
        (90, 0.7),
        (110, 0.5),
        (120, 0.4),
        (130, 0.3),
        (135, 0.2),
        (180, 0.1) #upwind
        ]

    angles.sort()
    position = bisect.bisect_right(angles, (diff_wind_boat,))
    sail_length = angles[position][1]
    return sail_length

def find_length(boat_compass, wind_direction):
    angle_boat_wind = calculate_angle_boat_wind(boat_compass, wind_direction)
    sail_length = assign_length(angle_boat_wind)
    return sail_length


#print(find_length(87, 180))

