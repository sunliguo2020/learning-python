# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/8 17:55
"""
import requests
from bs4 import BeautifulSoup

url = 'https://umei.net/bizhitupian/xiaoqingxinbizhi/'
domain=  'https://umei.net'

page  = requests.get(url)
page.encoding= 'utf-8'
#print(page.text)
main_page  = BeautifulSoup(page.text,'lxml')
a_list = main_page.find_all('a',attrs={'class':"TypeBigPics"})
#print(a_list)
for i in a_list:
    href = i.get('href')
    child_url = domain + href
    print(child_url)
    child_resp = requests.get(child_url)
    child_resp.encoding='utf-8'
    child_page = BeautifulSoup(child_resp.text)
    div = child_page.find(child_resp,attrs={'class':'ImageBody'})
    print(div)
    break
