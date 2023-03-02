import scrapy
from ..items import SavedataproItem
class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://ishuo.cn/duanzi']

    #基于终端指令的持久化存储
    # def parse(self, response):
    #     # 如何获取响应数据
    #     # 调用xpath方法对响应数据进行xpath形式的数据解析
    #     li_list = response.xpath('//*[@id="list"]/ul/li')
    #     all_data = []#爬取到的数据全部都存储到了该列表中
    #     for li in li_list:
    #         title = li.xpath('./div[2]/a/text()').extract_first()
    #         content = li.xpath('./div[1]/text()').extract_first()
    #         #将段子标题和内容封装成parse方法的返回
    #         dic = {
    #             'title':title,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #
    #     return all_data

    #基于管道的持久化存储
    def parse(self, response):
        # 如何获取响应数据
        # 调用xpath方法对响应数据进行xpath形式的数据解析
        li_list = response.xpath('//*[@id="list"]/ul/li')
        all_data = []  # 爬取到的数据全部都存储到了该列表中
        for li in li_list:
            title = li.xpath('./div[2]/a/text()').extract_first()
            content = li.xpath('./div[1]/text()').extract_first()
            #实例化一个item类型的对象
            item = SavedataproItem()
            #通过中括号的方式访问item对象中的两个成员，且将解析到的两个字段赋值给item对象的两个成员即可
            item['title'] = title
            item['content'] = content

            yield item #将存储好数据的item对象提交给管道
