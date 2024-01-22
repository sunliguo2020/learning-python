# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/22 21:10
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : curlconvert.py
 @Project : learning-python
"""
import requests

cookies = {
    'TMSESSNAME': 'c4855b70f21a623807c81c1d60a440f8',
    'tos_token': '5pYOUvz%40VXk28463BjF%21JfNxsrMowyhKiPDmnLIAcGtC%23daE%24eQZulSTRWq%2597Hb',
    'tos_visit_time': '1705929786',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://192.168.1.207:8181',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://192.168.1.207:8181/tos/index.php?user/login',
    'Token': '5pYOUvz@VXk28463BjF!JfNxsrMowyhKiPDmnLIAcGtC#daE$eQZulSTRWq%97Hb',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'name': 'admin',
    'check_code': 'undefined',
    'password': 'c3VuI2dhb0BHRTIwMjI=',
    'rember_password': '0',
}

response = requests.post(
    'http://192.168.1.207:8181/tos/index.php?user/loginSubmit',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)
cookies.update(response.cookies.get_dict())
print(cookies)
print(response.json())
print(requests.get('http://192.168.1.207:8181/tos/index.php',
                   headers=headers,
                   cookies=cookies).text)
