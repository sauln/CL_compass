# a short simulation that tests a running local web server
# this is kind of like a low key functional test 

import requests
import numpy as np
from compass import Compass
from user import User

def add_noise(singleton):
    return singleton + (5*np.random.random() - 2.5)

def build_user():
    current_location = {'lat': 0, 'lng': 0}
    new_user = User(current_location)
    return new_user

def build_compass(sale):
    compass = Compass(sale['coords'])
    return compass

def get_closest_sale(user):
    closest_sale = requests.get('http://127.0.0.1:5000/closest_sale',
                       params=user.current_location).json()
    print("Closest yard sale to me is at {}".format(closest_sale['coords']))
    return closest_sale

def follow_compass_towards_sale(user, compass):
    for i in range(10):
        direction = compass.get_direction_from_coords(user.current_location)
        direction = add_noise(direction)

        print("Headed {:2.3f} degrees, now at ({:.2f}, {:.2f})".format(direction,
                                                                  user.current_location['lng'],
                                                                  user.current_location['lat']))
        user.follow_the_compass(direction)

basic_user = build_user()
closest_sale = get_closest_sale(basic_user)
compass = build_compass(closest_sale)
follow_compass_towards_sale(basic_user, compass)

