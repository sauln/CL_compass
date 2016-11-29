
Scraper obviously runs on server,

Device:
* has own longitude and latitude
* asks for longitude and latitude of the yardsale closed to self
* computes angle between
* displays arrow w.r.t. device's compass.

- once it has the lng/lat of yardsale, it doesn't need to communicate
with the server until it requests a new yardsale

Server:
* returns longitude and latitude of yardsale closest to device
* if there are no yardsales close or all are old, try scraping new ones.

- server should not need to remember the device for main feature,
it might be fun to keep track of user stats so you can show things like
num of yardsales visited, num skipped, not missed out on. and have a leader 
board for yardsalers

#Yard sale app

- Scrape craigslist or other yard sale site for all yard sales
- Get current location
- Find closest yard sale 
- Point towards it

## More in-depth thoughts
- use opens up the app
- chooses a type of resource, default to yardsales
- send location and resource to server
- server looks for yardsales
- server returns top 10 closest yardsales
- Check when the most recent yard sale was posted - 
- Need to periodically scrape more data, maybe go to page 2

## Features
- Show the description of the post
- Designed as if there will be many concurrant connections
- Skip a yardsale, show the next closest if the yardsale looks like junk.
- showing the compass is great, but link to open up google maps directions is essential
  - automatically input current location -> yardsale directions
- show distance, euclidean is okay, but should probably replace with maps distance 

## Run

### The scrapper

```
cd $REPO\_ROOT/server/gatherer
scrapy crawl yardsale -o post_data/yardsales.jl
```

### Setup for compass

```
cd $REPO\_ROOT/server
python compass/ProcessSales.py
```

