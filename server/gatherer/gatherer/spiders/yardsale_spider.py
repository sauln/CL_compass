import scrapy

class YardsaleSpider(scrapy.Spider):
    name = 'yardsale'
    base_url = 'https://portland.craigslist.org'
    date = "2016-11-27"

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

        for url in good_links[:2]:
            yield scrapy.Request(self.base_url+url, callback=self.parse_post)

    def parse_post(self, response):
        # extract address data from post
        post = {
            'title': response.css('title::text').extract(),
            'address': response.xpath('//div[@class="mapaddress"]/text()').extract(),
            'url': response.url
        }

        self.log("Found the title of post page: %s"%post['title'])

        return post
