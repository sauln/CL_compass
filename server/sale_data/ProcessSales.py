''' script to run yardsale data through the google api to
    get the longitude and latitude
'''
import Util
from keys import key

# load the data as JSON lines
# get lng/lat for each post's address
# save as new JSON lines so compass can access

def AttachGeoData():
    infilename = 'server/gatherer/post_data/yardsales.jl'
    outfilename = 'server/sale_data/yardsales.jl'
    print("Loading json data from " + infilename)
    post_data = Util.load_post_data(infilename)
    print("Finding address coordinates for %s address" % post_data.__len__())

    for pid, post in enumerate(post_data):
        post['coords'] = Util.get_coords_of_address(post['address'], key)
        post['id'] = pid
        print(post)

    print("filter out address that google maps couldn't find easily")
    post_data = filter(lambda x: x['coords'] is not None, post_data)
    Util.save_post_data(post_data, outfilename)

    print("Printing new json to " + outfilename)

if __name__=="__main__":
    AttachGeoData()


