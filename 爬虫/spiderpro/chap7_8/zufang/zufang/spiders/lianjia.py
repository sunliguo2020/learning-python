import re

import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = [f'https://wf.lianjia.com/zufang/shouguangshi/pg{i}/#contentList' for i in range(1, 101)]

    def parse(self, response):
        full_url = ['https://wf.lianjia.com/' + url for url in
                    response.xpath('//div[@class="content__list--item--main"]/p/a[@class="twoline"]/@href').extract()]
        print(full_url)
        print(len(full_url))
        for item in full_url:
            yield scrapy.Request(url=item, callback=self.parse_info)

    def parse_info(self, response):
        title = response.xpath('//div[@class="content clear w1150"]/p/text()').get()
        total_price = response.xpath(
            '//div[@class="content__aside--title"]/span/text()|//div[@class="content__aside--title"]/text()').getall()
        price = ''.join(total_price).strip('')
        price = re.sub('\s', '', price)
        mode = response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').get()
        type = response.xpath('//ul[@class="content__aside__list"]/li[2]/text()').get()
        direction = response.xpath('//ul[@class="content__aside__list"]/li[3]/text()').get()
        print([title, price, mode, type, direction])
        yield {
            'title': title,
            "price": price,
            "mode": mode,
            "type": type,
            "direction": direction
        }
