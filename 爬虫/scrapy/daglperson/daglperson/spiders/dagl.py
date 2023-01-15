import scrapy

from scrapy import Request


class DaglSpider(scrapy.Spider):
    name = 'dagl'
    allowed_domains = ['127.0.0.1:8000']
    start_urls = ['http://127.0.0.1:8000/personid/list/?page=123']

    def parse(self, response):

        list_items = response.xpath('//tr/td[2]/a')
        for list_item in list_items:
            url = list_item.xpath('@href')
            url = response.urljoin(url.extract_first())
            print(url)
            yield Request(url=url, callback=self.parse_none, dont_filter=True)

        next_url = response.xpath('//ul[@class="pagination"]/li[last()-2]/a/@href').get()

        next_url = response.urljoin(next_url)

        if next_url:
            yield Request(url=next_url, callback=self.parse, dont_filter=True)

    def parse_none(self, response):
        pass
