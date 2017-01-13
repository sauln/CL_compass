'''
Compass supplies server side functions for generating coordinates from
street addresses.

Some client side code is mixed in here currently.
'''

import math
import unittest

import numpy as np
# get current location
# get closest yardsale
# get direction to closest yardsale

class Compass():
    ''' Compass will always point towards towards'''
    def __init__(self, towards):
        self.towards = towards
        self.current_coords = {'lat':0, 'lng':0}
        self.direction = self._compute_direction()

    def __str__(self):
        return "Compass always pointing towards {}".format(self.towards)

    def _set_current_coords(self, current_coords):
        self.current_coords = current_coords

    def get_direction_from_coords(self, current_coords):
        self._set_current_coords(current_coords)
        self.direction = self._compute_direction()
        return self.direction

    def get_direction(self, current_coords):
        return self.get_direction_from_coords(current_coords)

    def _compute_direction(self):
        rise = self.towards['lat'] - self.current_coords['lat']
        run  = self.towards['lng'] - self.current_coords['lng']
        direction = math.degrees( math.atan2(rise, run) )
        return direction

    def get_distance_from_coords(self, current_coords):
        sale_loc = np.array( [self.towards['lat'], self.towards['lng']] )
        src_loc = np.array( [current_coords['lat'], current_coords['lng']] )
        return np.linalg.norm(src_loc-sale_loc)

    def get_distance(self, current_coords):
        return self.get_distance_from_coords(current_coords)


class TestCompass(unittest.TestCase):
    def setUp(self):
        self.start = {'lat':0, 'lng':0}
        self.ends = [({'lng': 0,'lat': 1},   90.0),
                    ({'lng': 1,'lat': 0},    0.0),
                    ({'lng': 0,'lat':-1},  -90.0),
                    ({'lng':-1,'lat': 0},  180.0),
                    ({'lng': 1,'lat': 1},   45.0),
                    ({'lng':-1,'lat':-1}, -135.0),
                    ({'lng':-1,'lat': 1},  135.0),
                    ({'lng': 1,'lat':-1},  -45.0)]

    def test_distance(self):
        for end in self.ends:
            c = Compass(end[0])
            distance= c.get_distance(self.start)
            solution = math.sqrt(math.fabs(end[0]['lat']) +
                                 math.fabs(end[0]['lng']))
            self.assertEqual(distance, solution)

    def test_direction(self):
        # comfirm the direction is correct
        for end in self.ends:
            c = Compass(end[0])
            direction = c.get_direction_from_coords(self.start)
            self.assertEqual(direction, end[1])

if __name__=="__main__":
    unittest.main()

