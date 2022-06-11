import scrapy
from ..items import DeepproItem

class DeepSpider(scrapy.Spider):
    name = 'deep'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest']
    url_model = 'https://wz.sun0769.com/political/index/politicsNewest?id=1&page=%d'
    page_num = 2
    #解析首页数据
    def parse(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            title = li.xpath('./span[3]/a/text()').extract_first()
            detail_url = 'https://wz.sun0769.com'+li.xpath('./span[3]/a/@href').extract_first()
            # print(title)
            item = DeepproItem()
            item['title'] = title
            #对详情页的url发起请求
            #参数meta可以将自身这个字典传递给callback指定的回调函数
            yield scrapy.Request(meta={'item':item},url=detail_url,callback=self.parse_detail)
        if self.page_num < 3:
            new_url = format(self.url_model%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
    #解析详情页数据
    def parse_detail(self,response):
        meta = response.meta #接收请求传参过来的meta字典
        item = meta['item']
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]//text()').extract()
        content = ''.join(content)
        # print(content)
        item['content'] = content

        yield item
