import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JianliSpider(CrawlSpider):
    name = 'jianli'
    #allowed_domains = ['jianli.com']
    start_urls = ['https://sc.chinaz.com/jianli/free.html']

    rules = (
        Rule(LinkExtractor(allow=r'index*.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
