# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-29 22:46
"""
import requests
from lxml import etree

url = 'https://music.163.com/discover/toplist?id=19723756'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers= headers)
# print(resp.text)
xpath_str = etree.HTML(resp.text)
a_list = xpath_str.xpath('//a[contains(@href,"/song")]')
for i in a_list:
    a = i.xpath('./text()')
    print(a)
