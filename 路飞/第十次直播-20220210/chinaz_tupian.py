# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/11 10:45
"""
import requests
from lxml import etree

url = 'https://sc.chinaz.com/tupian/meinvtupian.html'
page_response = requests.get(url)
page_response.encoding = 'utf-8'
page_text = page_response.text
# print(page_text)

tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@id="container"]/div')
print(div_list)
img_urls = []
for div in div_list:
    img_url = "https:" + div.xpath('.//a/img/@src2')[0]
    img_name = div.xpath('.//p/a/text()')[0]
    img_urls.append(img_url)
    print(img_url, img_name)
    req = requests.get(url=img_url).content
    with open('img/' + img_name + '.jpg', 'wb') as fp:
        fp.write(req)
