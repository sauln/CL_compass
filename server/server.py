import numpy as np
import json

from flask import Flask
from flask import request
import compass

app = Flask(__name__)

filename = 'server/compass/sales/yardsales.jl'
post_data = compass.load_post_data(filename)

def distance(x, y):
    return np.linalg.norm(x-y)

def distance_sale(x, sale):
    sale_loc = np.array( [sale['coords']['lat'], sale['coords']['lng']] )
    d = distance(x, sale_loc)
    return distance(x, sale_loc)

@app.route("/")
def home():
    return "<title>This will describe the API that is exposed</title>\
            Get the closest sale with 127.0.0.1:5000/closest_sale?lat=XXX&lng=XXX<br>\
            Portland's (lat, lng) are just about (44.52, -122.68)<br><br>\
            How do you simulate a user?"

@app.route("/closest_sale", methods=['GET'])
def get_closest_sale():
    lat = request.args.get('lat', '')
    lng = request.args.get('lng', '')

    if lat and lng:
        lat, lng = float(lat), float(lng)
        # load all sales and find nearest sale
        current_location = np.array([lat, lng])
        closest = min(post_data, key=lambda x: distance_sale(current_location, x))
        return json.dumps(closest)
    else:
        return "No coordinates"

if __name__ == "__main__":
    app.run(debug=True)

