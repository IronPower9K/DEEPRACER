import math

class PARAMS:
    prev_speed = None
    prev_steps = None
    prev_direction_diff = None
    prev_normalized_distance_from_route = None


def reward_function(params):

    

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    is_offtrack = params['is_offtrack']
    speed = params['speed']
    steps = params['steps']

    if PARAMS.prev_steps is None or steps < PARAMS.prev_steps:
        PARAMS.prev_speed = None
        PARAMS.prev_direction_diff = None
        PARAMS.prev_normalized_distance_from_route = None
    
    

    reward =1.0

    
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]


    track_direction = math.atan2(next_point[1]-prev_point[1],next_point[0]-prev_point[0])
    

    track_direction=math.degrees(track_direction)
   
    
    
    direction_diff= abs(track_direction - heading)
    
    
    has_speed_dropped = False
    if PARAMS.prev_speed is not None:
        if PARAMS.prev_speed > speed:
            has_speed_dropped = True

    if has_speed_dropped:
        reward*=0.1
    
    

    
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

   
    if direction_diff < 5.0:
        speed>3.0
        reward*=1.3

    elif direction_diff < 7.5:
        speed>2.5
        reward *= 0.8
    
    elif direction_diff < 15:
        speed>1.5
        reward *=0.5
   
    else:
       reward *=0.3
    

    has_Direction_low = False
    if PARAMS.prev_direction_diff is not None:
        if PARAMS.prev_direction_diff > direction_diff:
            has_Direction_low = True



    if has_Direction_low is True:
        reward *= 2
    
    if is_offtrack:
        reward =1e-3




    PARAMS.prev_speed = speed
    PARAMS.prev_direction_diff = direction_diff
    PARAMS.prev_steps = steps

    return float(reward)
