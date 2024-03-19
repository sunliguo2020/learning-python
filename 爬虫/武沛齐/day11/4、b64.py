# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/15 20:19
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 4、b64.py
 @Project : learning-python
"""
import base64

userAccount = 'wupeiqi'
print(userAccount.encode('utf-8'))
userAccount_b64 = base64.b64encode(userAccount.encode('utf-8'))
print(userAccount_b64)

password = '112233'
password_b64 = base64.b64encode(password.encode('utf-8'))
print(password_b64)
