#TODO
Need to dev the app.

React is a pain, want to learn Java, so do an Android native app.




#Yard sale app
- Get current location
- Find closest yard sale - scrape craigslist or other yard sale site for all yard sales 
in the city or w/in N miles.
- Point towards sale - interface with handheld device's internal compass to find 
direction w.r.t. North. 

## Design:
**Device:**
* has own longitude and latitude
* asks for longitude and latitude of the yardsale closest to self
* computes angle between - constantly
* displays arrow w.r.t. device's compass.
* once it has the lng/lat of yardsale, it doesn't need to communicate
with the server until it requests a new yardsale

**Server:**
* returns longitude and latitude of yardsale closest to device
* if there are no yardsales close or all are old, try scraping new ones.

## Soft features
* Skip a yardsale. Allow user to skip and go back to last sale.
* Access the title, description, and images of the post. 
* Open directions to yardsale in default maps.
* Open craigslist post.
* Indicate `freshness`
* Show distance
* Server should not need to remember the device for main feature
* It might be fun to keep track of user stats so you can show things like
num of yardsales visited, num skipped, not missed out on. and have a leader 
board for yardsalers

# Welcome devs

Contact Nathaniel Saul, nat at saulgill dot com

Clone the repo, setup a virtual env, install the requirements, run the following commands 
for maybe newest edits

## The scrapper

```
cd $REPO_ROOT/server/gatherer
scrapy crawl yardsale -o post_data/yardsales.jl
```

## Setup for compass

```
cd $REPO_ROOT
python server/sale_data/ProcessSales.py
```

## Run server
```
cd $REPO_ROOT
python server/server.py
```

