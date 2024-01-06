# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 15:59
"""
# match 必须第一位就匹配成功 否则失败 相当于search(^)
import re

print(re.search('\d', 'abc123'))
print(re.match('\d', 'abc123'))
