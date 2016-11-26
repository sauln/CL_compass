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

## Run scrapper

cd ~/development/yardsale/gatherer
`scrapy crawl yardsale -o post_data/yardsales.jl`
