'''
Compass supplies server side functions for generating coordinates from
street addresses.

Some client side code is mixed in here currently.
'''

import math
import unittest
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

    def set_current_coords(self, current_coords):
        self.current_coords = current_coords

    def get_direction_from_coords(self, current_coords):
        self.set_current_coords(current_coords)
        self.direction = self._compute_direction()
        return self.direction

    def _compute_direction(self):
        rise = self.towards['lat'] - self.current_coords['lat']
        run  = self.towards['lng'] - self.current_coords['lng']
        direction = math.degrees( math.atan2(rise, run) )
        return direction


class TestCompass(unittest.TestCase):
    def test_direction_correct(self):
        # comfirm the direction is correct

        start = {'lat':0, 'lng':0}
        ends = [({'lng': 0,'lat': 1},   90.0),
                ({'lng': 1,'lat': 0},    0.0),
                ({'lng': 0,'lat':-1},  -90.0),
                ({'lng':-1,'lat': 0},  180.0),
                ({'lng': 1,'lat': 1},   45.0),
                ({'lng':-1,'lat':-1}, -135.0),
                ({'lng':-1,'lat': 1},  135.0),
                ({'lng': 1,'lat':-1},  -45.0)]

        for end in ends:
            c = Compass(end[0])
            direction = c.get_direction_from_coords(start)
            self.assertEqual(direction, end[1])

if __name__=="__main__":
    unittest.main()

