# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/10 16:57
"""
import os

import requests
from lxml import etree

if not os.path.exists("girls"):
    os.makedirs("girls")
headers = {

}
url = 'https://pic.netbian.com/4kmeinv/'
page_response = requests.get(url)
page_response.encoding = 'gbk'
page_text = page_response.text

tree = etree.HTML(page_text)
#li_list = tree.xpath('//ul[@class="clearfix"]/li')
li_list = tree.xpath('//li')
for li in li_list:
    print(li.values)
    #img_title = li.xpath('./a/b/text()')[0] + '.jpg'
    #img_url = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    #print(img_title,img_url)
    """ img = requests.get(img_url).content
    with open("./girls/" + img_title, 'wb') as fp:
        fp.write(img)"""