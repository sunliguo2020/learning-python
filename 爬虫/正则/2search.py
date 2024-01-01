# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 15:51
"""
import re
# search 匹配一次，字符串中包含就可以
print(re.search('[a-z]', "123456a"))
print(re.search('[a-z]{2}', "123456ab"))
