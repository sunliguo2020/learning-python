# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/12 9:05
"""
import random

import requests
from lxml import etree

url = 'https://sc.chinaz.com/jianli/free.html'
page_response = requests.get(url=url)
page_response.encoding = 'utf-8'
page_text = page_response.text

# print(page_text)
tree = etree.HTML(page_text)
div_list = tree.xpath('//*[@id="container"]/div')
print(len(div_list))
for div in div_list:
    detail_a = "https:" + div.xpath('./a/@href')[0]
    print(detail_a)
    down_name =  div.xpath('./p/a/text()')[0]
    print(down_name)
    detail_response = requests.get(url=detail_a).text
    detail_tree = etree.HTML(detail_response)
    detail_ul = detail_tree.xpath('//*[@id="down"]/div[2]/ul/li')
    down_link = []
    for li in detail_ul:
        li_a = li.xpath('./a/@href')[0]
        #print(li_a)
        down_link.append(li_a)
    #print(down_link)
    link = random.choice(down_link)
    #print(link)
    down=  requests.get(link).content
    with open('./'+down_name+'.rar','wb') as fp:
        fp.write(down)

