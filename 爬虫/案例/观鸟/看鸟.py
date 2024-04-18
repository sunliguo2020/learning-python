# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/18 22:03
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import pprint
from urllib.parse import urlencode

import execjs
import requests

with open('demo1.js', encoding='utf-8') as fp:
    js_content = fp.read()

js_exec = execjs.compile(js_content)

b = {'page': '5',
     'limit': '20',
     'taxonid': '',
     'startTime': '',
     'endTime': '',
     'province': '青海省',
     'city': '',
     'district': '',
     'pointname': '',
     'username': '',
     'serial_id': '',
     'ctime': '',
     'taxonname': '',
     'state': '',
     'mode': '0',
     'outside_type': '0'}

# print(urlencode(b))
rest = js_exec.call('get_headers', urlencode(b))
# pprint.pprint(rest)

# 发送请求：
url = 'https://api.birdreport.cn/front/record/activity/search'
headers = rest.get('header')
headers[
    'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

proxy = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
resp = requests.post(url, headers=headers, data=rest.get('data'), proxies=proxy, verify=False)
print(resp.request.headers)
pprint.pprint(resp.json())
