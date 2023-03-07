# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/18 23:07
"""
import requests

url = 'https://www.288job.cn/job/'
resp = requests.get(url)
print(resp.text)
