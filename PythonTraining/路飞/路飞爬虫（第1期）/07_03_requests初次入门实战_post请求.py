# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-22 19:30
"""
import requests

url = 'https://fanyi.baidu.com/sug'

post_data = {
    'kw': 'dog'
}
resp = requests.post(url=url, data=post_data)
print(resp.json())
