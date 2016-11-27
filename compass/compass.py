import requests
import math

# get current location
# get closest yardsale
# get direction to closest yardsale

key = 'AIzaSyBIKDNUbNqHb5O5elHRMzq-_9sYDAqBid8'

def get_coords_of_address(address):
    ''' use google api to get long/lat from plain english address
    '''
    payload = {'address': address,
               'key':key
    }
    req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?',
                 params=payload)
    return req.json()['results'][0]['geometry']['location']

def get_current_location():
    ''' return current location mock '''
    home = '1600+Amphitheatre+Parkway,+Mountain+View,+CA'
    current_coords = get_coords_of_address(home)
    return current_coords

def get_direction_from_coords(current_coords, yardsale_location_coords):
    rise = yardsale_coords['lat'] - current_coords['lat']
    run = yardsale_coords['lng'] - current_coords['lng']

    direction = math.degrees( math.atan2(rise, run) )
    return direction

if __name__=="__main__":
    sale = '111 SW Harrison St, Portland, OR'
    yardsale_coords = get_coords_of_address(sale)
    current_coords = get_current_location()

    direction = get_direction_from_coords(current_coords, yardsale_coords)
    print(direction)


