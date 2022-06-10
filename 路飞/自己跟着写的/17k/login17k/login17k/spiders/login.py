import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['17k.com']
    shujia_url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
    login_url = 'https://passport.17k.com/ck/user/login'
    start_urls = [shujia_url]

    def start_requests(self):
        # 直接从 浏览器复制cookie
        # cookie_str = 'Cookie: GUID=e2104cbc-6b6d-41d9-8ea6-b023a689b6f0; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1647076036; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F12%252F92%252F32%252F93773292.jpg-88x88%253Fv%253D1647076189000%26id%3D93773292%26nickname%3Dtong192%26e%3D1662628326%26s%3D3e56ad4ff6e0e188; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2293773292%22%2C%22%24device_id%22%3A%2217f7d61ceb6bc-0bd38f7b85fd56-376b4502-1049088-17f7d61ceb76d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22e2104cbc-6b6d-41d9-8ea6-b023a689b6f0%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1647076887'
        # dic ={}
        # lst = cookie_str.split('; ')
        # for i in lst:
        #     k,v =i.split('=')
        #     dic[k] =v
        # yield scrapy.Request(url=self.start_urls[0],
        #                      cookies=dic,
        #                      callback=self.parse)
        # 走登陆流程
        login_url = 'https://passport.17k.com/ck/user/login'
        # username = '15689266171'
        # password = 'tongmingao1'
        # yield scrapy.Request(url=login_url, method='post',body="loginName=15689266171&password=tongmingao1")

        yield scrapy.FormRequest(url=login_url, method='post',
                                 formdata={"loginName": "15689266171",
                                           "password": "tongmingao1"}
                                 )

    def parse(self, response):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_detail)

        # print(response.text)

    def parse_detail(self, response):
        print(response.text)
