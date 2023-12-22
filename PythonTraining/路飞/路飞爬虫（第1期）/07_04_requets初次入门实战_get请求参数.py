# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-22 19:40
"""
import requests

url = 'https://movie.douban.com/j/chart/top_list'

data = {
    "type": 13,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
resp = requests.get(url, params=data, headers=headers)
print(resp.text)
