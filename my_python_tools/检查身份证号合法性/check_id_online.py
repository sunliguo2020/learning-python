# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/17 16:47
"""
import requests
from lxml import etree

with open('n3-sort.txt') as fp:
    for idcard in fp:
        #print(idcard.strip())
        id = idcard.strip()
        print(id)
        #requests.packages.urllib3.disable_warnings()
        header = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
        url = f'http://qq.ip138.com/idsearch/index.asp?userid={id}&action=idcard'
        print(url)
        resp = requests.get(url= url,headers=header,verify=False)
        resp.encoding='utf-8'
        selector = etree.HTML(resp.text)
        tbody = selector.xpath('/html/body/div/div[2]/div[2]/div[2]/div[2]/table/tbody/text()')
        print(tbody)

        #break
