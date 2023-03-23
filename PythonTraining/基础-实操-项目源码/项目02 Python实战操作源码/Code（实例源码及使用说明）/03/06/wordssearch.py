# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/12  15:15 
# 文件名称   ：wordssearch.PY
# 开发工具   ：PyCharm
'''
  如何对读取的文件内容进行分词
'''
import jieba # 导入jieba分词模块
filepath=input('请输入要读取的文件：') # 记录输入的文件路径
with open(filepath,encoding='utf-8') as f: # 打开文件
    words=jieba.lcut(f.read()) # 读取文件内容并分词
    print((''.join(words)).replace("\n", "")) # 替换换行符
