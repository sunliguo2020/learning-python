# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：checkversion.PY
# 开发工具   ：PyCharm
'''
  检测到Python版本不一致时自动退出程序
'''
import sys
# 检测Python版本号
__MAJOR, __MINOR, __MICRO = sys.version_info[0], sys.version_info[1], sys.version_info[2]
if __MAJOR < 3: # 判断主版本号是否小于3
    print('Python版本号过低，当前版本为 %d.%d.%d， 请重装Python解释器' % (__MAJOR, __MINOR, __MICRO))
    exit() # 退出程序