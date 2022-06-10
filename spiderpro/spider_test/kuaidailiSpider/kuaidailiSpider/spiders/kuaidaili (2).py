import scrapy

#创建爬虫类
class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://kuaidaili.com/free']

    def parse(self, response):
        # #print(response.text)
        # print(response.xpath('/html/body/div/div[4]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/text()').get())
        # print(response.xpath('//tr/td'))
        #提取IP PORT
        #选择所有的tr标签
        selecters = response.xpath('//tr')
        #遍历tr标签下的td标签
        for select in selecters:
            ip=select.xpath('./td[1]/text()').get()#在当前节点下继续选择和selecters
            port=select.xpath('./td[2]/text()').get()
            print([ip,port])

