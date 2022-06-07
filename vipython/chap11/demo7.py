# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/19 11:34
"""
try:
    a = int(input('请输入第一个整数:'))
    b = int(input('请输入第二个整数:'))
    result = a / b
except BaseException as e:
    print('程序出错了，',e)
else:
    print('结果为:',result)
