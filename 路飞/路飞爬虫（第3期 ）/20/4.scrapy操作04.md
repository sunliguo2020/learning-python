#### selenium+scrapy

- 需求：将网易新闻中的国内，国际，军事，航空四个板块下的新闻标题和内容进行数据爬取
  - 注意：哪些数据是动态加载的！
  - 技术：selenium，scrapy，中间件

- 分析：
  
  - 抓取首页中四个板块下所有的新闻标题和新闻内容
    - 获取首页中四个板块对应的详情页链接
      - 首页是没有动态加载数据，可以直接爬取+解析
  - 对每一个板块的url发起请求，获取详情页中的新闻标题等内容
    - 通过分析发现每一个板块中的新闻数据全部是动态加载的数据，如何解决呢？
      - 通过selenium解决
  
- scrapy+selenium的编码流程
  
  - 1.在爬虫文件中定义浏览器对象，将浏览器对象作为爬虫类的一个成员变量
  - 2.在中间件中通过spider获取爬虫文件中定义的浏览器对象，进行请求发送和获取响应数据
  - 3.在爬虫文件中重写一个closed方法，来关闭浏览器对象
  
- 爬虫文件

  - ```python
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
    
    ```

- 中间件文件：

  - ```python
    # Define here the models for your spider middleware
    #
    # See documentation in:
    # https://docs.scrapy.org/en/latest/topics/spider-middleware.html
    import requests
    from scrapy import signals
    
    # useful for handling different item types with a single interface
    from itemadapter import is_item, ItemAdapter
    from time import sleep
    from scrapy.http import HtmlResponse#scrapy封装的响应对象对应的类
    class WangyiproDownloaderMiddleware:
    
    
        def process_request(self, request, spider):
    
            return None
    
        def process_response(self, request, response, spider):
            #可以拦截到所有的响应对象
            #当前项目一共会产生多少个响应对象呢？
             #1 + 4 + n个响应对象，在这些响应对象中只有4这4个响应对象需要被修改
            #如何筛选出指定的4个板块对应的响应对象呢？
                #1.可以先找出指定4个板块的请求对象，然后根据请求对象定位指定4个响应对象
                #2.可以根据4个板块的url定位到四个板块的请求对象
            model_urls = spider.model_urls
            if request.url in model_urls:
                bro = spider.bro #从爬虫类中获取创建好的浏览器对象
                bro.get(request.url)
                sleep(1)
                # bro.execute_script('document.documentElement.scrollTo(0,9000)')
                # sleep(1)
                #获取动态加载的数据
                page_text = bro.page_source
                #说明该request就是指定响应对象的请求对象
                #此处的response就是指定板块对应的响应对象
                response = HtmlResponse(url=request.url,
                                        request=request,
                                        encoding='utf-8',
                                        body=page_text)
                                    #body就是响应对象的响应数据
                return response
            else:
                return response
    
        def process_exception(self, request, exception, spider):
           pass
    
    ```

- 配置文件：

  - ```python
    DOWNLOADER_MIDDLEWARES = {
        'wangyiPro.middlewares.WangyiproDownloaderMiddleware': 543,
    
    }
    ```

- 拓展功能：将人工智能+数据爬取中

  - 实现将爬取到的新闻进行分类和关键字提取

    - 百度AI的使用：https://ai.baidu.com/

      - 使用流程：

        - 点击首页右上角的控制台，进行登录。

        - 登录后进入到了智能云的首页

          - 点击页面左上角的三条杠，选择你想要实现的功能，点击，进入到指定功能页面

            - 在功能页面，首先点击【创建应用】，进行应用的创建
            - 创建好之后，点击管理应用就可以看到：
              - AppID，apiKey，secret key这三个值，会在程序中用到

          - 在功能页面点击左侧的【技术文档】，选择SDK说明，选择对应的Python语言即可，先看快速开始内容，在选择你想要实现的具体功能的文档界面即可。

            - 环境安装：pip install baidu-aip

          - 提取文章关键字：

            - ```
              from aip import AipNlp
              
              """ 你的 APPID AK SK """
              APP_ID = 'xxx'
              API_KEY = 'xxx'
              SECRET_KEY = 'xxx'
              
              client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
              
              title = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"
              
              content = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。"
              
              """ 调用文章标签 """
              result = client.keyword(title, content)
              for dic in result['items']:
                  if dic['score'] >= 0.8:
                      key = dic['tag']
                      print(key)
              ```

          - 文章分类：

            - ```
              from aip import AipNlp
              
              """ 你的 APPID AK SK """
              APP_ID = 'xxx'
              API_KEY = 'x'
              SECRET_KEY = 'xx'
              
              client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
              
              title = "秦刚访问特斯拉美国工厂马斯克陪同 传递什么信号？"
              
              content = "今天（4日），驻美大使秦刚访问了特斯拉硅谷工厂，同特斯拉CEO马斯克针对各项尖端科技、人类未来等主题展开探讨，并体验了特斯拉的新款Model S及最新自动辅助驾驶系统。他在海外社交平台上表示：“性能强劲，但乘坐平顺舒适”。"
              
              """ 调用文章分类 """
              result = client.topic(title, content)
              class_new = result['item']['lv1_tag_list'][0]['tag']
              print(class_new)
              ```

            

            
