# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/15 22:05
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 6.代码实现.py
 @Project : learning-python
"""
import requests
import ddddocr
from bs4 import BeautifulSoup



# 获取cookie
url = 'https://xuexi.chinabett.com/'
res = requests.get(url)
cookie_dict = res.cookies.get_dict()
print(cookie_dict)
content = res.content

# 找到验证码url

