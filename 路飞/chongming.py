# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/15 21:42
"""
import requests
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
search_url = 'https://msjw.gat.shandong.gov.cn/populationclient/search.shtml'
post_url = 'https://msjw.gat.shandong.gov.cn/populationclient/queryName.shtml'

resp = requests.get(url = search_url,headers =headers,verify=False)
print(resp.text)

