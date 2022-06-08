# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 11:07
"""

import requests

def download(url):
    resp =requests.get(url)
    print(resp.text)

if __name__ == "__main__":
    url  = 'http://www.xinfadi.com.cn/priceDetail.html'
    download(url)