# a short simulation that tests a running local web server
# this is kind of like a low key functional test 

import requests
import numpy as np

import Compass

current_location = {'lat': 0, 'lng': 0}
print("I am located at {}".format(current_location))

res = requests.get('http://127.0.0.1:5000')
assert "This will describe the API" in str(res.content)

res = requests.get('http://127.0.0.1:5000/closest_sale')
assert "No coordinates" in str(res.content)

res = requests.get('http://127.0.0.1:5000/closest_sale',
                   params=current_location).json()
print("Closest yard sale to me is at {}".format(res['coords']))
compass = Compass.Compass(res['coords'])

def follow_the_compass(location, direction):
    run = np.cos(np.radians(direction))
    rise = np.sin(np.radians(direction))
    print("    up: {:.3f}, over: {:.3f}".format(rise, run))
    location['lat'] += rise
    location['lng'] += run
    return location

for i in range(10):
    direction = compass.get_direction_from_coords(current_location)

    print("Headed {:2.3f} degrees, now at ({:.2f}, {:.2f})".format(direction,
                                                              current_location['lng'],
                                                              current_location['lat']))
    current_location = follow_the_compass(current_location, direction)

