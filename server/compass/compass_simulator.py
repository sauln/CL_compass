
# a short simulation that tests a running local web server
# this is like a unit test, right? 


import requests

coords = {'lat': 44.54, 'lng': -122.38}

res = requests.get('http://127.0.0.1:5000')
assert "This will describe the API" in str(res.content)

res = requests.get('http://127.0.0.1:5000/closest_sale')
assert "No coordinates" in str(res.content)




for i in range(10):
    res = requests.get('http://127.0.0.1:5000/closest_sale', params=coords)
    yardsale = res.json()

    print(res.json())



