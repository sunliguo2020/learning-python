# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-23 21:08
"""
import requests
import re

url = 'https://movie.douban.com/top250'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers = headers)
pageSource = resp.text
# print(pageSource)

# 编写正则表达式
obj  =re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>',re.S)
result = obj.finditer(pageSource)
for item in result:
    print(item.group('name'),item.group('pingfen'))