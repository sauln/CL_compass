from flask import Flask
from flask import request
import compass

app = Flask(__name__)

@app.route("/")
def home():
    return "This will describe the API that is exposed"

@app.route("/closest_sale", methods=['GET'])
def get_closest_sale():
    lat = request.args.get('lat', '')
    lng = request.args.get('lng', '')
    return "lat: {}<br>lng: {}".format(lat, lng)

if __name__ == "__main__":
    app.run()
