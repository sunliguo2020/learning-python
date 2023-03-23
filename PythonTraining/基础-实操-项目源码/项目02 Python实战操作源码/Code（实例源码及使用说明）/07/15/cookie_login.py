# *_* coding : UTF-8 *_*
# 文件名称   ：cookie_login.py
# 开发工具   ：PyCharm
import requests  # 导入网络请求模块
from lxml import etree  # 导入lxml模块

cookies = '此处填写登录后网页中的cookie信息'
headers = {'Host': 'www.douban.com',
           'Referer': 'https://www.hao123.com/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.121 Safari/537.36'}
# 创建RequestsCookieJar对象，用于设置cookies信息
cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    cookies_jar.set(key, value)  # 将cookies保存RequestsCookieJar当中
# 发送网络请求
response = requests.get('https://www.douban.com/', headers=headers, cookies=cookies_jar)
if response.status_code == 200:  # 请求成功时
    html = etree.HTML(response.text)  # 解析html代码
    # 获取用户名
    name = html.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]/text()')
    print('获取的帐号为：',name[0])  # 打印用户名