# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-23 21:40
"""
import re

import requests

url = 'https://dy2018.com/'
resp = requests.get(url)
resp.encoding = 'gbk'
# print(resp.text)
obj = re.compile(r'2023必看热片.*?<ul>(?P<html>.*?)</ul>',re.S)

result = obj.search(resp.text)
html = result.group('html')

obj2 = re.compile(r"<a href='.*?(?P<url>.*?)' title")
result2 = obj2.finditer(html)

for item in result2:
    print(item.group('url'))
