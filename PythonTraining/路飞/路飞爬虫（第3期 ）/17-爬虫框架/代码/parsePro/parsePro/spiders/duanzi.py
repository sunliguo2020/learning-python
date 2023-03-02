import scrapy

class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.xxx.com']
    #对首页进行网络请求
    #scrapy会对列表中的url发起get请求
    start_urls = ['https://ishuo.cn/duanzi']

    def parse(self, response):
        #如何获取响应数据
        #调用xpath方法对响应数据进行xpath形式的数据解析
        li_list = response.xpath('//*[@id="list"]/ul/li')
        for li in li_list:
            # content = li.xpath('./div[1]/text()')[0]
            # title = li.xpath('./div[2]/a/text()')[0]
            # #<Selector xpath='./div[2]/a/text()' data='一年奔波，尘缘遇了谁'>
            # print(title)#selector的对象，且我们想要的字符串内容存在于该对象的data参数里
            #解析方案1：
            # title = li.xpath('./div[2]/a/text()')[0]
            # content = li.xpath('./div[1]/text()')[0]
            # #extract()可以将selector对象中data参数的值取出
            # print(title.extract())
            # print(content.extract())
            #解析方案2：
            #title和content为列表，列表只要一个列表元素
            title = li.xpath('./div[2]/a/text()')
            content = li.xpath('./div[1]/text()')
            #extract_first()可以将列表中第0个列表元素表示的selector对象中data的参数值取出
            print(title.extract_first())
            print(content.extract_first())
