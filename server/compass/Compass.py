'''
Compass supplies server side functions for generating coordinates from
street addresses.

Some client side code is mixed in here currently.
'''

import math
from .Util import *

# get current location
# get closest yardsale
# get direction to closest yardsale

def get_current_location():
    ''' return current location mock '''
    home = '1600+Amphitheatre+Parkway,+Mountain+View,+CA'
    current_coords = Util.get_coords_of_address(home)
    return current_coords

def get_direction_from_coords(current_coords, yardsale_location_coords):
    rise = yardsale_coords['lat'] - current_coords['lat']
    run = yardsale_coords['lng'] - current_coords['lng']

    direction = math.degrees( math.atan2(rise, run) )
    return direction


if __name__=="__main__":
    sale = '111 SW Harrison St, Portland, OR'
    yardsale_coords = Util.get_coords_of_address(sale)
    current_coords = get_current_location()

    direction = get_direction_from_coords(current_coords, yardsale_coords)
    print(direction)

