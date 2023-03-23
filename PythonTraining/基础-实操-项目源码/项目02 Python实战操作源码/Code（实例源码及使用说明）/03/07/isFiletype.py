# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/8  11:21 
# 文件名称   ：isFiletype.PY
# 开发工具   ：PyCharm
'''
  对数据分析时只能选择Excel或者CSV文件
'''
def istype(filetype):
    '''
    判断是否为Excel或者CSV文件
    :param filetype: 文件扩展名
    :return: 是，返回True，不是，返回False
    '''
    filetype = filetype.lower() # 扩展名转换为小写
    if filetype == '.xls': # 判断是否为.xls
        return True # 返回True
    elif filetype == '.xlsx': # 判断是否为.xlsx
        return True
    elif filetype == '.csv': # 判断是否为.csv
        return True
    else:
        return False
import os
while True:
    path=input('输入要判断的文件名：') # 记录输入的路径
    filetype = os.path.splitext(path)[1]  # 获取扩展名
    if istype(filetype):  # 判断是否为数据表格文件
        print('您选择的文件符合数据分析的文件格式……')
    else:
        print('选择的文件不是数据表格格式！')