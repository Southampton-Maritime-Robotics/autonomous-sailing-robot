import bisect

def calculate_angle_boat_wind(boat_compass, wind_direction):
    angle = abs(boat_compass - wind_direction)
    if angle > 180:
        angle = 360 - angle
    return angle


def assign_length(diff_wind_boat):
    angles = [
        (30, 1),
        (40, 2),
        (50, 3),
        (60, 4),
        (70, 5),
        (80, 6),
        (90, 7),
        (110, 8),
        (120, 9),
        (130, 10),
        (140, 11),
        (150, 12),
        (180, 13),
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

