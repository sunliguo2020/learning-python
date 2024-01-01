# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-30 10:22
"""

import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.baidu.com')

bs = BeautifulSoup(page.content, features='lxml')
print(bs.title)
print(bs.findAll('a'))
print(bs.find_all('a'))
