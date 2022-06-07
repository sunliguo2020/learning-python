# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/8 11:33
"""
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '9999':
        print('密码正确！')
        break
    else:
        print('密码不正确！')
else:
    print('对不起，3次密码均输入错误。')
