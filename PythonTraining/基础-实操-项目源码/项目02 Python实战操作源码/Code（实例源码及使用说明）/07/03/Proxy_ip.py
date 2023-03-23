# *_* coding : UTF-8 *_*
# 文件名称   ：Proxy_ip.py
# 开发工具   ：PyCharm

import requests  # 导入网络请求模块
from lxml import etree  # 导入HTML解析模块

# 头部信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.121 Safari/537.36'}
# 发送网络请求
response = requests.get('https://www.xicidaili.com/nn/',headers=headers)
response.encoding = 'utf-8'           # 设置编码方式
if response.status_code == 200:       # 判断请求是否成功
    html = etree.HTML(response.text)  # 解析HTML
    table = html.xpath('//table[@id="ip_list"]')[0]  # 获取table标签内容
    trs = table.xpath('//tr')[1:]  # 获取所有tr标签，排除第一条
    # 循环遍历标签内容
    for t in trs:
        ip = t.xpath('td/text()')[0]  # 获取代理ip
        port = t.xpath('td/text()')[1]  # 获取端口
        print('代理ip为：',ip, '对应端口为：', port)