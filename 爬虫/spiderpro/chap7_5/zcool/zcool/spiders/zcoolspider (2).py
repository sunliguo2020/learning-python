import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ZcoolItem


class ZcoolspiderSpider(CrawlSpider):
    name = 'zcoolspider'
    allowed_domains = ['zcool.com.cn']
    start_urls = ['https://www.zcool.com.cn/?p=1#tab_anchor']

    rules = (
        Rule(LinkExtractor(allow=r'/?p=\d+#tab_anchor'), follow=False),
        Rule(LinkExtractor(allow=r'/work/.+=.html'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        img_urls = response.xpath('//div[@class="work-show-box js-work-content"]//img/@src').getall()
        title_list = response.xpath('//h2/text()').getall()
        title = "".join(title_list).strip()

        # print(img_urls)
        # print(title_list)

        item = ZcoolItem(image_urls=img_urls, title=title)
        print(item)
        yield item
