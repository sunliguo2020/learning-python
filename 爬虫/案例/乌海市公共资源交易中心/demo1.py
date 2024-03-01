# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/25 20:03
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

url = 'http://www.whggzy.com/portal/category'
headers = {
    "Referer": "http://www.whggzy.com/site/category?parentId=65999&childrenCode=ImportantNotice&utm=site.site-PC-49434.1497-pc-wsg-customArticlePurchaseNoticeList-front.1.a0821b00d3d511eeacff57819e712be0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=utf-8",
    "X-Requested-With": "XMLHttpRequest"
}
data_str = '{"pageNo": 3, "pageSize": 15, "categoryCode": "ImportantNotice", "_t": 1708862527000}'
data = {"pageNo": 3, "pageSize": 15, "categoryCode": "ImportantNotice", "_t": 1708862527000}
resp = requests.post(url=url, headers=headers, json=data)
# resp = requests.post(url=url, headers=headers, data=data_str)
print(resp.text)
