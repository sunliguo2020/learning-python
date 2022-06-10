import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        print(response.xpath('//title/text()'))
