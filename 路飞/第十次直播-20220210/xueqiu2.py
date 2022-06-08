# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/12 9:47
"""
import requests
session = requests.Session()
url = 'https://xueqiu.com/statuses/hot/listV2.json'
parms = {
    "since_id": "-1",
    "max_id": "312107",
    "size": "15"
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}
resp = session.get(url = "https://xueqiu.com",params=parms,headers=headers)
resp2 = session.get(url = url,params=parms,headers=headers)
print(resp2.json())