# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/9/5 7:16
"""
import requests

url = 'https://www.so.com/s'
params = {'q': 'python'}

resp = requests.get(url, params=params)
print(dir(resp))
# resp.encoding='utf-8'
#print(resp.text)
print(resp.headers)
print(resp.reason)
print(resp.status_code)
print(type(resp.content))