# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 16:31
"""
import re

data = re.search('\w','absd123s')
print(data)
print(data.group())
print(data.groups()) # 返回括号的内容
