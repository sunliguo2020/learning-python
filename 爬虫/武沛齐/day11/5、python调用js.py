# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/15 21:38
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 5.py
 @Project : learning-python
"""
import execjs

with open('v3.js', 'r', encoding='utf-8') as fp:
    js_content = fp.read()

js = execjs.compile(js_content)

result = js.call('base64encode', 'wupeiqi')
print(result)

password = js.call('base64encode', '112233')

pwd_en = js.call('encryptPwd', password)
print(pwd_en)
