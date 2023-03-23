# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/8  18:46 
# 文件名称   ：thumbnail.PY
# 开发工具   ：PyCharm
'''
  按照京东运营要求将图片批量处理为指定大小
'''
from PIL import Image
import os  # 导入os模块

while True: # 循环输入
    path=input('请输入图片所在路径：') # 记录输入的路径
    width=int(input('请输入宽度限制：'))
    height=int(input('请输入高度限制：'))
    try:
        list = os.listdir(path)  # 遍历选择的文件夹
        for i in range(0, len(list)):  # 遍历文件列表
            filepath = os.path.join(path, list[i])  # 记录遍历到的文件名
            image = Image.open(filepath) # 打开图片文件
            # 按指定大小对图片进行缩放（不一定完全按照设置的宽度和高度，而是按比例缩放到最接近的大小）
            image.thumbnail((width, height))
            # 下面的方法会以严格按指定大小对图片进行缩放，但可能会失真
            # image = image.resize((width, height))
            image.save(filepath) # 保存缩放后的图片
        print('图片处理完成……')
        os.startfile(path) # 打开指定路径进行预览
    except Exception as e:
        print(e)

