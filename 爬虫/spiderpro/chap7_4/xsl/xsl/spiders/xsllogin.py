import scrapy


class XslloginSpider(scrapy.Spider):
    name = 'xsllogin'
    allowed_domains = ['xslou.com']
    #start_urls = ['http://xslou.com/']
    def start_requests(self):
        url = 'https://www.xslou.com/login.php'
        form_data={

        }


    def parse(self, response):
        pass
