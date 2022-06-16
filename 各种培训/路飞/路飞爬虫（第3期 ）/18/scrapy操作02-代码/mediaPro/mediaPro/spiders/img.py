import scrapy
from ..items import MediaproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src').extract_first()
            item = MediaproItem()
            item['src'] = img_src

            yield item