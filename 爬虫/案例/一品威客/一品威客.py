# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/14 12:15
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""

import execjs
import requests

username = '15689266171'
password = '123456'
with open('./demo1.js') as fp:
    js_code = fp.read()

js_compile = execjs.compile(js_code)
U = js_compile.call("fn", username, password)

print(U)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Access-Token': '',
    'App-Id': '4ac490420ac63db4',
    'App-Ver': '',
    'CHOST': 'www.epwk.com',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Device-Os': 'web',
    'Device-Ver': '',
    'Imei': '',
    'NonceStr': str(U.get('NonceStr')),
    'Origin': 'https://www.epwk.com',
    'Os-Ver': '',
    'Pragma': 'no-cache',
    'Referer': 'https://www.epwk.com/login.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Signature': U.get('Signature'),
    'Timestemp': str(U.get('Timestemp')),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-REQUEST-ID': 'b3d8eac16ac9c37a927e7d1405c298fe',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'username': username,
    'password': password,
    'code': '',
    'hdn_refer': 'https://zt.epwk.com/',
}

response = requests.post('https://www.epwk.com/api/epwk/v1/user/login',
                         # cookies=cookies,
                         headers=headers,
                         data=data)
print(response.text)
