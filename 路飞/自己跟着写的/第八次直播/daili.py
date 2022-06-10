# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/5 9:09
"""
import requests
# 只爬取了第一页的内容
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
url = 'https://www.kuaidaili.com/free'
page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, 'lxml')
trs = soup.select('tbody > tr')
for tr in trs:
    t1 = tr.findAll('td')[0]
    t2 = tr.findAll('td')[1]
    ip = t1.string
    port = t2.string
    print(ip, port)
