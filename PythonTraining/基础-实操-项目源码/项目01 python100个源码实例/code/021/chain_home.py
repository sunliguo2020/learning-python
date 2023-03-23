'''
爬取链家网
'''

from fake_useragent import UserAgent  # 导入伪造头部信息的模块
import asyncio  # 异步io模块
import aiohttp  # 异步网络请求模块
import requests  # 导入网络请求模块
from lxml import etree  # 导入lxml解析html的模块
import pandas  # 导入pandas模块


class HomeSpider():  # 链家爬虫的类
    def __init__(self):  # 初始化
        self.data = []  # 创建数据列表
        self.headers = {"User-Agent": UserAgent().random}  # 随机生成浏览器头部信息

    async def request(self, url):  # 异步网络请求的方法
        async with aiohttp.ClientSession() as session:  # 创建异步网络请求对象
            try:
                # 根据传递的地址发送网络请求
                async with session.get(url, headers=self.headers, timeout=3) as response:
                    print(response.status)
                    if response.status == 200:  # 如果请求码为200说明请求成功
                        result = await response.text()  # 获取请求结果中的文本代码
                        return result
            except Exception as e:
                print(e.args)  # 打印异常信息

    def get_page_all(self, city):  # 请求一次，获取租房信息的所有页码
        city_letter = self.get_city_letter(city)  # 获取城市对应的字母
        url = 'https://{}.lianjia.com/zufang/ab200301001000rco11rt200600000001rs{}/'.format(city_letter, city)
        response = requests.get(url, headers=self.headers)  # 发送网络请求
        if response.status_code == 200:
            html = etree.HTML(response.text)  # 创建一个XPath解析对象
            # 获取租房信息的所有页码
            page_all = html.xpath('//*[@id="content"]/div[1]/div[2]/@data-totalpage')[0]
            print('租房信息总页码获取成功！')
            return int(page_all) + 1
        else:
            print('获取租房信息所有页码的请求未成功！')

    # 解析数据
    async def parse_data_all(self, page_all, city):
        for i in range(1,page_all):  # 根据租房信息的总页码，分别对每一页信息发送网络请求
            city_letter = self.get_city_letter(city)  # 获取城市对应的字母
            url = 'https://{}.lianjia.com/zufang/ab200301001000pg{}rco11rt200600000001rs{}/'.format(city_letter,i, city)
            html_text = await self.request(url)  # 发送网络请求，获取html代码
            html = etree.HTML(html_text)  # 创建一个XPath解析对象
            print('获取'+url+'页信息！')
            title_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[1]/a/text()')  # 获取每页中所有标题
            big_region_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/a[1]/text()')  # 获取每页中所有大区域
            small_region_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/a[2]/text()')  # 获取每页中所有小区域
            square_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/text()[5]')  # 获取每页中所有房子的面积
            floor_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/span/text()[2]')  # 获取每页中所有房子的楼层
            price_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/span/em/text()')  # 获取每页中所有房子的价格
            title_list = self.remove_spaces(title_all)  # 删除标题信息中的空格与换行符
            region_list = self.combined_region(big_region_all, small_region_all)  # 组合后的区域信息
            square_list = self.remove_spaces(square_all)  # 删除面积信息中的空格与换行符
            floor_list = self.remove_spaces(floor_all)  # 删除楼层信息中的空格与换行符
            price_list = self.remove_spaces(price_all)  # 删除价格信息中的空格与换行符
            # 每页数据
            data_page = {'title': title_list,
                         'region': region_list,
                         'price': price_list,
                         'square': square_list,
                         'floor': floor_list}
            print('写入第'+str(i)+'页数据！')
            df = pandas.DataFrame(data_page)              # 创建DataFrame数据对象
            df.to_csv('{}租房信息.csv'.format(city),mode='a', encoding='utf_8_sig',index=None)  # 写入每页数据


    # 删除字符串中的空格与换行符
    def remove_spaces(self, info):
        info_list = []  # 保存去除空格后的字符串
        for i in info:  # 循环遍历包含空格信息
            x=i.replace(' ', '').replace('\n', '')
            if x =='':
                pass
            else:
                info_list.append(x)  # 将去除空格后的字符串添加至列表中
        return info_list  # 返回去除空格后的信息

    # 获取北、上、广城市名称对应的字母
    def get_city_letter(self, city_name):
        city_dict = {'北京': 'bj', '上海': 'sh', '广州': 'gz'}
        return city_dict.get(city_name)  # 返回城市名称对应的英文字母

    # def get_city_letter(self, city_name):
    #     city_dict = {'北京': 'bj', '上海': 'sh', '广州': 'gz','深圳':'sz'}
    #     return city_dict.get(city_name)  # 返回城市名称对应的英文字母

    # 将大区域小区域合并
    def combined_region(self, big_region, small_region):
        region_list = []  # 保存组合后的区域信息
        # 循环遍历大小区域，并将区域组合
        for a, b in zip(big_region, small_region):
            region_list.append(a + '-' + b)
        return region_list

    # 启动异步
    def start(self, page_all, city):
        loop = asyncio.get_event_loop()      # 创建loop对象
        # 开始运行
        loop.run_until_complete(self.parse_data_all(page_all, city))


if __name__ == '__main__':
    input_city = input('请输入需要下载租房信息的城市名称！')
    home_spider = HomeSpider()  # 创建爬虫类对象
    page_all = home_spider.get_page_all(input_city)  # 获取所有页码
    print(page_all)    # 打印所有页码信息
    home_spider.start(page_all, input_city)          # 启动爬虫程序
