# This will be a mock for the signals between the device and the compass


class User():
    ''' '''
    def __init__(self, current_location):
        self.current_location = current_location

    def where_am_i(self):
        return "I am located at {}".format(current_location)

    def follow_the_compass(self, direction):
        run = np.cos(np.radians(direction))
        rise = np.sin(np.radians(direction))
        print("    up: {:.3f}, over: {:.3f}".format(rise, run))
        self.current_location['lat'] += rise
        self.current_location['lng'] += run

