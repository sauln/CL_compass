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
    print("Loading json data from " + infilename)

    post_data = Util.load_post_data(infilename)

    print("Finding address coordinates for %s address" % post_data.__len__())

    pid = 0

    for post in post_data:
        print(post)
        post['coords'] = Util.get_coords_of_address(post['address'], key)
        post['id'] = pid
        pid += 1

    post_data = filter(post_data, lambda x: x['coords'] == "OK")

    outfilename = 'server/sale_data/yardsales.jl'

    Util.save_post_data(post_data, outfilename)

    print("Printing new json to " + outfilename)

if __name__=="__main__":
    AttachGeoData()


