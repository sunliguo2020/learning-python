# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/1 8:55
"""
import requests

chinaunicom_news_url = "http://www.chinaunicom.com.cn/api/article/NewsByIndex/4/2022/11/news"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
req = requests.get(chinaunicom_news_url, headers=headers)
print(dir(req))
print(req.json())
