import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("响应对象为：",response.text)
