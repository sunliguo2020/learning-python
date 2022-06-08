import scrapy


class BaidumidSpider(scrapy.Spider):
    name = 'baidumid'
    #allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        #print('baidu')
        print(response.xpath('//title/text()').extract_first())
