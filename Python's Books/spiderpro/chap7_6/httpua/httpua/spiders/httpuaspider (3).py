import scrapy


class HttpuaspiderSpider(scrapy.Spider):
    name = 'httpuaspider'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print(response.text)
        yield  scrapy.Request(self.start_urls[0],dont_filter=True)
