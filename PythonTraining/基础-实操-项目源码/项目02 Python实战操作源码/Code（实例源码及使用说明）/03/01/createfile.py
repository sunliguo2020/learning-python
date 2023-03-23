# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/9  9:31 
# 文件名称   ：createfile.PY
# 开发工具   ：PyCharm
'''
  以当前日期时间创建文件
'''
import datetime
import os
import time

while True:
    path = input('请输入文件保存地址：')  # 记录文件保存地址
    num = int(input('请输入创建文件的数量：'))  # 记录文件创建数量
    # 循环创建文件
    for i in range(num):
        t = datetime.datetime.now()  # 获取当前时间
        # 对当前日期时间进行格式化，作为文件名
        file = os.path.join(path, t.strftime('%Y%m%d%H%M%S') + '.txt')
        open(file, 'w', encoding='utf-8')  # 以UTF8编码创建文件
        time.sleep(1)  # 休眠1秒钟
        i += 1  # 循环标识加1
    print('创建成功！')
    os.startfile(path)  # 打开路径查看
