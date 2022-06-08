import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MycwpjtItem


class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['sohu.com']
    start_urls = ['http://sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?/n.*?shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i =  MycwpjtItem()
        i['name'] = response.xpath('/html/head/title/text()').extract_first()
        i['link'] =response.xpath('//link[@rel="canonical"]/@href').extract_first()
        print(response)
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        yield i
