# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-13 18:00
"""
import hashlib
import time

import requests

res = requests.get('https://bbs.pku.edu.cn/v2/home.php')
cookie_dict = res.cookies.get_dict()
print(cookie_dict)

# 2、登录
user = "zhangkai"
pwd = '123123'
ctime = int(time.time())
data_string = f"{pwd}{user}{ctime}{pwd}"
obj = hashlib.md5()

obj.update(data_string.encode('utf-8'))
md5_string = obj.hexdigest()

res = requests.post('https://bbs.pku.edu.cn/v2/ajax/login.php',
                    data={
                        "username": user,
                        'password': pwd,
                        "keepalive": 0,
                        'time': ctime,
                        't': md5_string
                    },
                    cookies=cookie_dict,
                    )
print(res.text)
