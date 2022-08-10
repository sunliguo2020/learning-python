# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/12/8 21:58
"""
import requests

url = 'http://www.baidu.com'

resp = requests.get(url)
resp.encoding = 'utf-8'
cookie = resp.cookies
headers = resp.headers

print(resp.text)
