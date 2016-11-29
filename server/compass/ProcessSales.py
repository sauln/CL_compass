''' script to run yardsale data through the google api to
    get the longitude and latitude
'''
import Util
import json

# load the data as JSON lines
# get lng/lat for each post's address
# save as new JSON lines so compass can access

infilename = 'gatherer/post_data/yardsales.jl'
print("Loading json data from " + infilename)

post_data = []
with open(infilename, 'r') as f:
    for line in f:
        post_data.append(json.loads(line))

print("Finding address coordinates for %s address" % post_data.__len__())

for post in post_data:
    post['coords'] = Util.get_coords_of_address(post['address'])

outfilename = 'compass/sales/yardsales.jl'
with open(outfilename, 'w') as f:
    for post in post_data:
        f.write(json.dumps(post)+"\n")

print("Printing new json to " + outfilename)

