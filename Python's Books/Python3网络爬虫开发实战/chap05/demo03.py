# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/1 21:40
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

url = 'https://spa1.scrape.center'
html = requests.get(url).text
print(html)
