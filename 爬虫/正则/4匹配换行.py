# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 16:18
"""
import re

myStr = """
<a href="http://www.baidu.com">百度</a>
<a href="http://www.aqiyi.com">爱奇艺</a>
<A href="http://www.aqiyi.com">爱奇艺2</A>
<a href="http://www.taobao.com">淘
宝</a>
"""

print(re.findall('<a href=.*?>.*?</a>', myStr, re.S|re.I))
