import scrapy

from ..items import DeepimgproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['xx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']
    url_model = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    page = 2

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        # print(response.txt)
        li_list = response.xpath('//div[@class="slist"]/ul/li')
        for li in li_list:
            title = li.xpath('./a/b/text()').extract_first()
            detail_url = "https://pic.netbian.com/" + li.xpath('./a/@href').extract_first()
            # print(detail_url)
            pic_url = "https://pic.netbian.com/" + li.xpath('./a/img/@src').extract_first()
            #print(pic_url)
            item = DeepimgproItem()
            item['img_src'] = pic_url
            yield item

        #手动发起深度请求
        if self.page <100:
            new_url = self.url_model % self.page
            print(new_url)
            yield scrapy.Request(url=new_url,callback=self.parse)
            self.page += 1
            # yield scrapy.Request(url=detail_url, callback=self.detail_parse)

    def detail_parse(self, response):
        img_url = "https://pic.netbian.com/" + response.xpath('//*[@id="img"]/img/@src').extract_first()
        # print(img_url)
