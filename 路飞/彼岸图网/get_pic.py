# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/18 21:18
"""
from lxml import etree
import requests

url = "https://pic.netbian.com/4kfengjing/"
resp = requests.get(url = url)
resp.encoding = 'gbk'
page_text = resp.text
#print(page_text)
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]//li')
#print(li_list)
for i in li_list:
    a= "https://pic.netbian.com"+i.xpath('./a/@href')[0]
    #print(a)
    child_resp = requests.get(a)
    child_resp.encoding='gbk'
    child_text = child_resp.text
    child_tree = etree.HTML(child_text)
    pic_name = child_tree.xpath('//*[@id="img"]/img/@title')[0]+".jpg"
    pic_url = "https://pic.netbian.com"+child_tree.xpath('//*[@id="img"]/img/@src')[0]
    #print(pic_name,pic_url)
    with open(pic_name,"wb") as fp:
        fp.write(requests.get(pic_url).content)
    print(pic_name,"下载完成！")


