import scrapy

from ..items import PagesproItem
class PageSpider(scrapy.Spider):
    name = 'page'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']

    url_model = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    page_num = 2
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            img_src = li.xpath('./a/img/@src').extract_first()
            img_name = li.xpath('./a/b/text()').extract_first()
            # print(img_name,img_src)
            item = PagesproItem()
            item['title'] = img_name
            item['src'] = img_src

            yield item

        if self.page_num < 3: #结束递归的条件
            new_url = self.url_model % self.page_num
            self.page_num += 1
            #手动请求发送
            yield scrapy.Request(url=new_url,callback=self.parse)
