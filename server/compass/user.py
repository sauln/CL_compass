# This will be a mock for the signals between the device and the compass
import unittest
import numpy as np

from compass import Compass

class User():
    ''' '''
    def __init__(self, current_location):
        self.current_location = current_location

    def where_am_i(self):
        return self.current_location

    def follow_the_compass(self, direction):
        run = np.cos(np.radians(direction))
        rise = np.sin(np.radians(direction))
        self.current_location['lat'] += rise
        self.current_location['lng'] += run

class TestUser(unittest.TestCase):
    def setUp(self):
        self.origin = {'lat':0, 'lng':0}
        self.user = User(self.origin)

    def test_where_am_i(self):
        self.assertEqual(self.user.where_am_i(), self.origin)

    def test_heads_in_right_direction(self):
        compass = Compass({'lat':10, 'lng':10})
        curr_dist = compass.get_distance_from_coords(self.user.where_am_i())
        self.user.follow_the_compass(compass.get_direction(self.user.where_am_i()))
        new_dist = compass.get_distance_from_coords(self.user.where_am_i())
        self.assertLess(new_dist,curr_dist)

if __name__=="__main__":
    unittest.main()


