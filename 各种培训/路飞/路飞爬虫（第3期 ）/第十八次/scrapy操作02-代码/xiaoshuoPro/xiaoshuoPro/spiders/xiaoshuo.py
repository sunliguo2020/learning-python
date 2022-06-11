import scrapy

from ..items import XiaoshuoproItem
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.shicimingju.com/book/xiyouji.html']

    def parse(self, response):
        li_list = response.xpath('//*[@id="main_left"]/div/div[4]/ul/li')
        for li in li_list:
            title = li.xpath('./a/text()').extract_first()
            item = XiaoshuoproItem()
            item['title'] = title

            yield item