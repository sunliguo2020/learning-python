# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/4 19:54
"""
import requests

head = {
    'user-agent':"Mozilla"
}
img_src = 'http://img.itlun.cn/uploads/allimg/180506/1-1P5061TS6-lp.jpg'

response = requests.get(url=img_src,headers=head)

with open('./123.jpg','wb') as fp:
    fp.write(response.content)