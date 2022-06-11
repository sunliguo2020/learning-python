import scrapy
from ..items import WangyiproItem
from selenium import webdriver
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    #创建浏览器对象，把浏览器对象作为爬虫类的一个成员
    bro = webdriver.Chrome(executable_path='/Users/zhangxiaobo/Desktop/三期/chromedriver1')

    model_urls = [] #存储4个板块对应的url
    def parse(self, response):
        #从首页解析每一个板块对应详情页的url，将其存储到model_urls列表中
        model_index = [2,3,5,6]
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        for index in model_index:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
        #应该对每一个板块的详情页发起请求（动态加载）
        for model_url in self.model_urls:
            yield scrapy.Request(url=model_url,callback=self.parse_detail)
    #目的是为了解析出每一个板块中的新闻标题和新闻详情页的url
    def parse_detail(self,response):
        #response就是一个不符合需求要求的响应对象
            #该response中没有存储动态加载的新闻数据，因此该响应对象被视为不符合要求的响应对象
            #需要将不符合要求的响应对象变为符合要求的响应对象即可，如何做呢？
            #方法：篡改不符合要求的响应对象的响应数据，将该响应对象的响应数据修改为包含了动态加载的新闻数据即可。
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            try:
                #解析新闻标题+新闻详情页的url
                title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
                new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
                item = WangyiproItem()
                item['title'] = title
            except Exception as e:
                print('遇到了广告，忽略此次行为即可！')

            #对新闻的详情页发起请求
            if new_detail_url != None:
                yield scrapy.Request(url=new_detail_url,callback=self.new_content_parse,meta={'item':item})

    def new_content_parse(self,response):
        item = response.meta['item']
        #解析新闻的详情内容
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content).strip()
        item['content'] = content

        yield item

    #重写一个父类方法，close_spider，该方法只会在爬虫最后执行一次
    def closed(self,spider):
        #关闭浏览器
        print('关闭浏览器成功！')
        self.bro.quit()
