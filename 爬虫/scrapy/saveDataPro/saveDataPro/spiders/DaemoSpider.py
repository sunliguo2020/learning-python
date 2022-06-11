import scrapy


class DaemospiderSpider(scrapy.Spider):
    name = 'DaemoSpider'
    allowed_domains = ['xx.com']
    start_urls = ['http://xx.com/']

    def parse(self, response):
        pass
