# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/8  13:04 
# 文件名称   ：getfilesystems.PY
# 开发工具   ：PyCharm
'''
  遍历指定文件夹下的所有子文件夹及文件
'''
import os  # 导入os模块
while True: # 循环输入
    path=input('请输入一个路径：') # 记录输入的路径
    try:
        list = os.listdir(path)  # 遍历选择的文件夹
        filenames=[] # 存储所有文件的列表
        dirnames=[] # 存储所有子文件夹的列表
        for i in range(0, len(list)):  # 遍历文件列表
            filepath = os.path.join(path, list[i])  # 记录遍历到的文件名
            if os.path.isdir(filepath): # 判断是否为文件夹
                dirnames.append(list[i]) # 将遍历到的文件夹添加到列表中
            elif os.path.isfile(filepath):  # 判断是否为文件
                filenames.append(list[i]) # 将遍历到的文件添加到列表中
        print('\033[1;41m————文件夹列表————\033[0m')
        for dirname in dirnames: # 遍历子文件夹列表并输出
            print('  ',dirname)
        print('\033[1;42m—————文件列表—————\033[0m')
        for filename in filenames: #遍历文件列表并输出
            print('  ',filename)
    except:
        print('请输入一个有效路径……')