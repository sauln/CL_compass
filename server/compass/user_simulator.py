# a short simulation that tests a running local web server
# this is kind of like a low key functional test 

import requests
import numpy as np
import Compass


class User():
    ''' '''
    def __init__(self, current_location):
        self.current_location = current_location

    def follow_the_compass(self, direction):
        run = np.cos(np.radians(direction))
        rise = np.sin(np.radians(direction))
        print("    up: {:.3f}, over: {:.3f}".format(rise, run))
        self.current_location['lat'] += rise
        self.current_location['lng'] += run

    def where_am_i(self):
        return "I am located at {}".format(current_location)

def add_noise(singleton):
    return singleton + (5*np.random.random() - 2.5)

current_location = {'lat': 0, 'lng': 0}
user = User(current_location)

res = requests.get('http://127.0.0.1:5000/closest_sale',
                   params=user.current_location).json()


# deny this first post 




print("Closest yard sale to me is at {}".format(res['coords']))
compass = Compass.Compass(res['coords'])

for i in range(10):
    direction = compass.get_direction_from_coords(user.current_location)
    direction = add_noise(direction)

    print("Headed {:2.3f} degrees, now at ({:.2f}, {:.2f})".format(direction,
                                                              current_location['lng'],
                                                              current_location['lat']))
    user.follow_the_compass(direction)

