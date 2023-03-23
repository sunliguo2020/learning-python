# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/8  10:39 
# 文件名称   ：getfilename.PY
# 开发工具   ：PyCharm
'''
  批量提取文件名保存到一个文件中
'''
import os  # 导入os模块

with open('D:\Test.txt', 'a') as f: # 以追加方式打开文件
    path=input('请输入要提取名称的文件所在路径：') # 记录输入的路径
    try:
        list = os.listdir(path)  # 遍历选择的文件夹
        for i in range(0, len(list)):  # 遍历文件列表
            filename=os.path.splitext(list[i])[0] # 提取文件名
            f.write(filename+'\n') # 将提取的文件名写入文本文件
        print('文件名提取完成 ')
    except:
        print('请输入一个有效路径……')