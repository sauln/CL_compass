# a short simulation that tests a running local web server
# this is kind of like a low key functional test 

import requests
import numpy as np
from compass import Compass
from user import User

def add_noise(singleton):
    return singleton + (5*np.random.random() - 2.5)

current_location = {'lat': 0, 'lng': 0}
user = User.User(current_location)
res = requests.get('http://127.0.0.1:5000/closest_sale',
                   params=user.current_location).json()

print("Closest yard sale to me is at {}".format(res['coords']))
compass = Compass.Compass(res['coords'])

for i in range(10):
    direction = compass.get_direction_from_coords(user.current_location)
    direction = add_noise(direction)

    print("Headed {:2.3f} degrees, now at ({:.2f}, {:.2f})".format(direction,
                                                              current_location['lng'],
                                                              current_location['lat']))
    user.follow_the_compass(direction)

