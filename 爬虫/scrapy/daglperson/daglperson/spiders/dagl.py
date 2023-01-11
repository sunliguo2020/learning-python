import scrapy
scrapy.http.response
from scrapy import Request
from scrapy.selector import Selector


class DaglSpider(scrapy.Spider):
    name = 'dagl'
    allowed_domains = ['127.0.0.1:8000']
    start_urls = ['http://127.0.0.1:8000/personid/list/']

    def parse(self, response):
        # sel = Selector(response)
        # next_url = sel.xpath('//ul[@class="pagination"]/li[14]/a/@href')
        # print(next_url)
        # print(next_url.extract_first())
        for i in range(1, 91477):
            next_url = f'?page={i}'
            next_url = response.urljoin(next_url)
            if next_url:
                yield Request(url=next_url, callback=self.content_parse, dont_filter=True)

    def content_parse(self, response):
        sel = Selector(response)
        # list_items = sel.css('body > div:nth-child(2) > div > div.bs-example > div.panel.panel-default > table > tbody > tr:nth-child(1) > td:nth-child(3) > a')
        list_items = sel.xpath('/html/body/div[1]/div/div[3]/div[1]/table/tbody/tr')
        for list_item in list_items:
            url = list_item.xpath('./td[2]/a/@href')
            # print(url.extract_first())
            url = response.urljoin(url.extract_first())
            print(url)
            yield Request(url=url,callback=self.content_parse,dont_filter=True)
