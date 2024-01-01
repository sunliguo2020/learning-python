# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 17:23
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./douban.html', 'r', encoding='utf-8'), 'lxml')
# print(type(soup))
# print(soup.title)
# print(soup.title.string)
# print(soup.div)
# print(soup.a)
# print(soup.p)
# print(soup.div['id'])
# print(soup.div['class'])
# print(soup.div.attrs)
# print(soup.title)
# print(soup.title.text)
# print(soup.title.string)
# print(soup.title.get_text().strip())

# print(soup.div)
# print(soup.find("div", attrs={'class': 'top-nav-info'}))
# print(soup.find('div',class_ = 'top-nav-info'))

# print(soup.find('li',class_="poster"))
print(soup.find('li', class_="poster").a.img.get('src'))
print(soup.find('li', class_="poster").a.img.attrs)
