import scrapy

from ..items import DuanziItem


class DuanziSpider(scrapy.Spider):
    name = 'Duanzi'
    # allowed_domains = ['ishuo.com']
    start_urls = ['https://ishuo.cn/duanzi']

    def parse(self, response):

        all_data = []
        li_list = response.xpath('//div[@id="list"]/ul/li')
        for li in li_list:
            content = li.xpath('./div[1]/text()').extract()[0]
            title = li.xpath('./div[2]/a/text()').extract()[0]
            # print(title)
            # print(content)
            # dict = {"title": title,
            #         "content": content
            #         }
            # all_data.append(dict)
            item = DuanziItem()
            item['title'] = title
            item['content'] = content
            #print(item)

            yield item