import bisect

def calculate_angle_boat_wind(boat_compass, wind_direction):
    angle = abs(boat_compass - wind_direction)
    if angle > 180:
        angle = 360 - angle
    return angle


def assign_length(diff_wind_boat):
    angles = [
        (30, 1), #downwind
        (40, 0.95),
        (50, 0.9),
        (60, 0.85),
        (70, 0.8),
        (80, 0.7),
        (90, 0.6),
        (110, 0.5),
        (120, 0.4),
        (130, 0.3,
        (140, 0.2),
        (150, 0.15),
        (180, 0.1), #upwind
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

