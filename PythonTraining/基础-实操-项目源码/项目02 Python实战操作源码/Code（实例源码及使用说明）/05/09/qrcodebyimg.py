# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：qrcodebyimg.PY
# 开发工具   ：PyCharm
'''
  生成仿微信公众号推广的个性二维码（支持动态）
'''
from MyQR import myqr
# 要生成动态二维码，只需要将piture参数和save_name参数设置gif动图即可
myqr.run(
    words='https://www.mingrisoft.com', # 指定二维码包含的文本
    picture="logo.jpg",  # 指定底图
    colorized=True, # 指定为彩色
    save_name='qrcodebyimg.png' # 指定保存名称
)
