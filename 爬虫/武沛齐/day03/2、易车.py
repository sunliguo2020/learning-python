# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-14 8:35
"""
import requests
from bs4 import BeautifulSoup


res = requests.get('http://car.yiche.com')
# print(res.status_code)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
tag = soup.find_all('div', attrs={'class': 'brand-name'})

for t in tag:
    print(t.text)
