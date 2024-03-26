# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/22 20:59
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

r = requests.get('http://www.baidu.com')

print(r.cookies)

for key, value in r.cookies.items():
    print(key + '=' + value)
