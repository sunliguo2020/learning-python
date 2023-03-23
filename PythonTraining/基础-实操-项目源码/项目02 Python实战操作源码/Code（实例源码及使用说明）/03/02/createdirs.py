# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/8  13:54 
# 文件名称   ：createfiles.PY
# 开发工具   ：PyCharm
'''
  如何根据文件中存储的产品型号批量生成相应文件夹
'''
import os # 导入os模块
path='D:\\' # 要创建文件夹的路径
# 以只读方式打开文件
with open('product.txt','r',encoding='utf-8') as f:
    for line in f.readlines(): # 读取所有行
        dirpath=path+line.strip() # 拼接要创建的文件夹路径
        if not os.path.exists(dirpath): # 判断路径不存在
            os.mkdir(dirpath) # 创建文件夹
print('创建完成……')
os.startfile(path) # 打开路径

