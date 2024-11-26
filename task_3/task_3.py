import math

def time_diff(time_from, time_to):
    angle_from = 2 * math.pi * time_from / 24
    angle_to = 2 * math.pi * time_to / 24
    
    angle_diff = abs(angle_to - angle_from)
    
    if angle_diff > math.pi:
        angle_diff = 2 * math.pi - angle_diff
    
    return int(round(angle_diff * 24 / (2 * math.pi)))
