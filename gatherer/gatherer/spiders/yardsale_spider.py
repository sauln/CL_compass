import scrapy

class Yardsale():
    def __init__(self, title, address, url):
        self.title=title
        self.address=address
        self.url=url


class YardsaleSpider(scrapy.Spider):
    name = 'yardsale'
    base_url = 'https://portland.craigslist.org'
    date = "2016-11-26"

    yardsale_url = [
        base_url + '/search/gms'
    ]

    start_urls = [url+"?sale_date="+date for url in yardsale_url]

    def parse(self, response):
        title = response.css('title::text').extract()
        self.log("Found the title: %s"%title)
        return self.parse_page(response)

    def parse_page(self, response):
        all_links = response.xpath('//a[@class="result-title hdrlnk"]/@href').extract()
        good_links = filter(lambda x: "craigslist.org" not in x, all_links)

        for url in good_links[:3]:
            yield scrapy.Request(self.base_url+url, callback=self.parse_post)

    def parse_post(self, response):
        # do stuff with the post page
        title = response.css('title::text').extract()
        address = response.xpath('//div[@class="mapaddress"]').extract()
        url = response.url
        yardsale = Yardsale(title, address, url)
        self.log("Found the title of post page: %s"%title)

