import requests

key = 'AIzaSyBIKDNUbNqHb5O5elHRMzq-_9sYDAqBid8'

def get_coords_of_address(address):
    ''' use google api to get long/lat from plain english address
    '''
    payload = {'address': address,
               'key':key
    }
    req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?',
                 params=payload)

    coords = req.json()['results'][0]['geometry']['location']
    return coords
