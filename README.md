#Yard sale app

- Get current location
- Find closest yard sale - scrape craigslist or other yard sale site for all yard sales 
in the city or w/in N miles.
- Point towards sale - interface with handheld device's internal compass to find 
direction w.r.t. North. 

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
* Choose a type of resource, default to yardsales
* Include other sites. Not just craigslist.
* Access the title, description, and images of the post. 
* Indicate `freshness`, 
	(check when the most recent yard sale was posted)
* Assume lots of users will use this at one time. 
	(caching information, concurrent connections, ...)
* Assume low power devices.
	(most processing on server)
* Assume low storage devices.
	(most storage on server, what is biggest impact data to be fast, ...)
* Skip a yardsale. Allow user to skip to last sale and go back.
* Open maps directions is essential.
  	(automatic input of directions in desired app)
* Open craigslist post.
* Show distance
	(euclidean okay, how intense to replace with map's distance?)
* Server should not need to remember the device for main feature
	(accessible 
* It might be fun to keep track of user stats so you can show things like
num of yardsales visited, num skipped, not missed out on. and have a leader 
board for yardsalers
* Server looks for yardsales periodically, caches results for all users
* Need to periodically scrape more data, maybe go to page 2 of craigslist

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
python server/compass/ProcessSales.py
```

## Run server
```
cd $REPO_ROOT
python server/server.py
```





