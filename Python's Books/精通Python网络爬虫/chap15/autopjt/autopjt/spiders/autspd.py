import scrapy
from ..items import AutopjtItem

class AutspdSpider(scrapy.Spider):
    name = 'autspd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4006497.html']

    def parse(self, response):
        item = AutopjtItem()
        li_list = response.xpath('//ul[@id="component_47"]/li')
        #print(ul_list)
        for li in li_list:
            name = li.xpath('.//a[@dd_name="单品标题"]/text()').extract_first()
            price = li.xpath('.//p[@class="price"]/span/text()').extract_first()
            link = li.xpath('.//a[@dd_name="单品标题"]/@href').extract_first()
            comnum = li.xpath('./p[@class="star"]/a/text()').extract_first()
            #item(name = name,price=price,link =link,comnum = comnum)
            item['name'] =name
            item['price'] =price
            item['link'] =link
            item['comnum'] =comnum

            yield item
        
        for i in range(1,20):
            print("正在爬取第",i,"页")
            url = f'http://category.dangdang.com/pg{i}-cid4006497.html'
            yield scrapy.Request(url,callback=self.parse)
        #print(response)
