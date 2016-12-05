import scrapy

class YardsaleSpider(scrapy.Spider):
    name = 'yardsale'
    base_url = 'https://portland.craigslist.org'
    date = "2016-12-4"

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

        for url in good_links:
            yield scrapy.Request(self.base_url+url, callback=self.parse_post)

    def parse_post(self, response):
        # extract address data from post
        post = {
            'title': response.css('title::text').extract_first(),
            'address':
            response.xpath('//div[@class="mapaddress"]/text()').extract_first(),
            'url': response.url
        }

        self.log("Found the title of post page: %s"%post['title'])

        return post
