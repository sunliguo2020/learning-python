# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/22 21:04
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

s = requests.Session()
response = s.get('https://www.httpbin.org/cookies/set/number/12345678')
print(response.cookies)
print(s.cookies)
r = s.get('https://www.httpbin.org/cookies')
print(r.text)
print(s.cookies)
