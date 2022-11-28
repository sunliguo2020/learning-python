# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/19 11:28
"""
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0哦!')
except ValueError:
    print("不能将字符串转换为数字")
except BaseException as e:
    print(e)
print('程序结束！！！')