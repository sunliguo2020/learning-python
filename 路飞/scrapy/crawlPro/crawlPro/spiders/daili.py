import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DailiSpider(CrawlSpider):
    name = 'daili'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    rules = (
        Rule(LinkExtractor(allow=r'/free/inha/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
