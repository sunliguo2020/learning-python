# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-17 16:38
"""
import requests

url = 'https://so.gushiwen.cn/RandCode.ashx'
res = requests.get(url)
with open('code.jpg', 'wb') as f:
    f.write(res.content)
