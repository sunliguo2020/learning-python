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

