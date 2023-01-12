import scrapy

class FirstSpider(scrapy.Spider):
    #爬虫名称：爬虫文件唯一标识：可以使用该变量的值来定位到唯一的一个爬虫文件
    name = 'first' #无需改动
    #允许的域名：scrapy只可以发起百度域名下的网络请求
    # allowed_domains = ['www.baidu.com']
    #起始的url列表：列表中存放的url可以被scrapy发起get请求
    start_urls = ['https://www.baidu.com/','https://www.sogou.com']

    #专门用作于数据解析
    #参数response：就是请求之后对应的响应对象
    #parse的调用次数，取决于start_urls列表元素的个数
    def parse(self, response):
        print('响应对象为：',response)
