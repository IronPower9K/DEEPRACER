import math

# 108등
def reward_function(params):

  

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    is_offtrack = params['is_offtrack']
    speed = params['speed']


    reward =1.0

    
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]


    track_direction = math.atan2(next_point[1]-prev_point[1],next_point[0]-prev_point[0])
    

    track_direction=math.degrees(track_direction)
   
    
    
    direction_diff= abs(track_direction - heading)
    
    
    

    
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

   
    if direction_diff < 5.0:
        speed>4.0

    if direction_diff < 7.5:
        speed>3.0
        reward *= 0.8
    elif direction_diff < 15:
        speed>2.0
        reward *=0.5
   
    else:
       reward *=0.3
    
    
    if is_offtrack:
        reward =1e-3

    speed_limit1 = 1.0
    speed_limit2 = 3.0


    if speed < speed_limit1:
        reward *= 0.5
    elif speed < speed_limit2:
        reward *= 0.8   

    return float(reward)
