# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-14 8:49
"""
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
res = requests.get('https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD',
                   headers=headers)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
parent_tag = soup.find('ul', {'id': 'm-pl-container'})
# print(parent_tag)
for child in parent_tag.find_all(recursive=False):
    # print(child)
    title = child.find('a', {'class': 'tit f-thide s-fc0'}).text
    img_url = child.find('img')['src']
    print(title, img_url)
    # break
