import requests
#from .keys import key
import json

def get_coords_of_address(address, key):
    ''' use google api to get long/lat from plain english address
    '''
    payload = {'address': address,
               'key':key
    }
    req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?',
                 params=payload)

    coords = req.json()['results'][0]['geometry']['location']
    return coords

def save_post_data(post_data, outfilename):
    with open(outfilename, 'w') as f:
        for post in post_data:
            f.write(json.dumps(post)+"\n")

def load_post_data(infilename):
    post_data = []
    with open(infilename, 'r') as f:
        for line in f:
            post_data.append(json.loads(line))

    return post_data

