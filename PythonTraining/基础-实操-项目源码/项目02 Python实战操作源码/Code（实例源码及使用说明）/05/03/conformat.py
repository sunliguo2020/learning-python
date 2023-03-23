# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/9  13:29 
# 文件名称   ：conformat.PY
# 开发工具   ：PyCharm
'''
  图片格式批量转换
'''
def istype(filetype):
    '''
    判断是否为图片文件
    :param filetype: 文件扩展名
    :return: 是，返回True，不是，返回False
    '''
    filetype = filetype.lower() # 扩展名转换为小写
    # 判断是否为图片格式
    if filetype == '.jpg' or filetype=='.jpeg' or filetype=='.png' or filetype=='.gif' or filetype=='.bmp' or filetype=='.tif':
        return True # 返回True
    else:
        return False
import os
from PIL import Image
while True:
    oldpath = input('请输入要转换格式的图片路径：')
    newpath = input('请输入转换格式后的图片保存路径：')
    flag = int(input('''要转换的格式：
1、jpg  2、jpeg  3、png  4、gif  5、bmp  6、tif
请选择：'''))
    list = os.listdir(oldpath)  # 遍历选择的文件夹
    for i in range(0, len(list)):  # 遍历文件列表
        filepath = os.path.join(oldpath, list[i])  # 记录遍历到的文件名
        if os.path.isfile(filepath):  # 判断是否为文件
            filename= os.path.splitext(list[i])[0]  # 获取文件名
            filetype = os.path.splitext(list[i])[1]  # 获取扩展名
            if istype(filetype):  # 判断是否为图片文件
                img = Image.open(filepath)  # 打开图片文件
                # 根据选择的格式转换图片，并保存
                if flag == 1:
                    img=img.convert('RGB') # 将图片转换为RGB格式，因为jpg格式不支持透明度
                    img.save(os.path.join(newpath,filename+'.jpg'),'jpeg')
                elif flag == 2:
                    img = img.convert('RGB')
                    img.save(os.path.join(newpath, filename + '.jpeg'),'jpeg')
                elif flag == 3:
                    img.save(os.path.join(newpath, filename + '.png'),'png')
                elif flag == 4:
                    img.save(os.path.join(newpath, filename + '.gif'),'gif')
                elif flag == 5:
                    img.save(os.path.join(newpath, filename + '.bmp'),'bmp')
                elif flag == 6:
                    img.save(os.path.join(newpath, filename + '.tif'), 'tiff')
    os.startfile(newpath)
    print('格式转换完成……')
