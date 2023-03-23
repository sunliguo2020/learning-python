# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：colourqrcode.PY
# 开发工具   ：PyCharm
'''
  如何使用qrcode批量生成不同颜色的二维码
'''
import qrcode
import random
import os
import pandas as pd

path=input('请输入保存路径：')
da = pd.DataFrame(pd.read_excel('qrcode.xlsx')) # 读取Excel
# 实例化二维码生成类
qr = qrcode.QRCode(
    version=1, # 控制二维码大小，范围为1——40
    # 错误纠正能力
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, # 控制每个小格子包含的像素数
    border=4, # 控制二维码与图片边界的距离
)
# 随机颜色
def rndColor():
    # 定义颜色列表（红、绿、蓝、紫、黑）
    list=['red','green','blue','purple','black']
    index=random.randint(0,len(list)-1) # 随机生成索引
    return list[index] # 按索引返回颜色
i=0 # 循环标识
while i < len(da.values): # 遍历数据
    qr.clear() # 清空二维码设置的数据
    # 设置二维码数据
    qr.add_data(data=da.values[i][1])
    # 启用二维码颜色设置
    qr.make(fit=True)
    # 以随机生成的颜色生成二维码
    img = qr.make_image(fill_color=rndColor(), back_color="white")
    # 保存二维码图片
    img.save(os.path.join(path, da.values[i][0] + '.png'))
    i+=1 # 循环标识加1
print('生成完成，请查看！')
os.startfile(path) # 打开路径进行查看
