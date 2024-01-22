# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/22 21:51
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 测试.py
 @Project : learning-python
"""
import requests

url = 'http://192.168.1.207:8181/tos/index.php?share/common_js'

resp = requests.get(url)
print(resp.cookies.get_dict())
