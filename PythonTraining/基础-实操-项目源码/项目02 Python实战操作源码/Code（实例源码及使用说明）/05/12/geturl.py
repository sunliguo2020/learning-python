# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：geturl.PY
# 开发工具   ：PyCharm
'''
  验证二维码链接地址
'''
import zxing
import os
from PIL import Image

reader = zxing.BarCodeReader() # 创建二维码识别对象
# 在当前目录生成临时文件，避免路径问题
def getqrcodeinfo(filename):
    img = Image.open(filename) # 打开二维码图片
    img.save('%s.png' % os.path.basename(filename).split('.')[0]) # 建立临时文件
    qrcodeinfo = reader.decode('%s.png' % os.path.basename(filename).split('.')[0])  # 图片解码
    # 删除临时文件
    os.remove('%s.png' % os.path.basename(filename).split('.')[0])
    if qrcodeinfo: # 判断是否有数据
        return qrcodeinfo

while True:
    path = input('请输入要验证的二维码图片所在路径：') # 记录输入的路径
    list = os.listdir(path)  # 遍历选择的文件夹
    for i in range(0, len(list)):  # 遍历文件列表
        filepath = os.path.join(path, list[i])  # 记录遍历到的文件名
        if os.path.isfile(filepath):  # 判断是否为文件
            filetype = os.path.splitext(list[i])[1]  # 获取扩展名
            # 判断是否为图片文件
            if filetype == '.jpg' or filetype=='.jpeg' or filetype=='.png' or filetype=='.gif' or filetype=='.bmp' or filetype=='.tif':
                print(list[i],'——',getqrcodeinfo(filepath).parsed)
