# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：getCode.PY
# 开发工具   ：PyCharm
'''
  生成高考填报志愿时的姓名区位码
'''
def getCode(chinese):
    '''
    获取汉字对应区位码
    :param chinese: 单个汉字
    :return: 获取到的区位码
    '''
    barray = chinese.encode('gb2312') # 用GB2312对汉字进行编码
    # 计算区位码(如果是1位，则格式为2位)
    code = '{0:02d}'.format((barray[0] - 160)) + '{0:02d}'.format((barray[1] - 160))
    return code # 返回区位码

while True: # 循环输入
    name = input('请输入姓名：') # 记录输入的姓名
    for word in name: # 遍历输入的姓名
        print(word,':',getCode(word)) # 输入单个汉字及对应区位码

