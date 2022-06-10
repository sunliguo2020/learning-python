# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/29 16:41
"""
import requests

url =  'http://www.sogou.com'

response = requests.get(url)
print(type(response))
print(dir(response))
#print(response.text)
page_text = response.text

with open('./sougou.html','w') as fp:
    fp.write(page_text)
print("数据爬取  存储成功")