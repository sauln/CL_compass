''' script to run yardsale data through the google api to
    get the longitude and latitude
'''
import Util
import json

# load the data
# run each one through the thang

post_data = []
with open('gatherer/post_data/yardsales.jl', 'r') as f:
    for line in f:
        post_data.append(json.loads(line))


for post in post_data:
    post['coords'] = Util.get_coords_of_address(post['address'])

import pdb; pdb.set_trace()

