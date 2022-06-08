# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/9/5 18:08
"""
import requests

url = 'https://www.xslou.com/login.php'
data = {'username': '18600605736', 'password': '57365736', 'action': 'login'}
resq = requests.post(url, data=data)
resq.encoding = 'gb2312'
print(resq.status_code)
print(resq.text)
