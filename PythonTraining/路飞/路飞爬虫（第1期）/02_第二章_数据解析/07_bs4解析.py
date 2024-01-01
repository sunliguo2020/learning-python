# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-23 22:25
"""
from bs4 import BeautifulSoup

html = """
<ul>
    <li><a href='zhangwuji.com'>张无忌</a></li>
    <li><a href='zhangwuji.com'>张无忌</a></li>
    <li><a href='zhangwuji.com'>张无忌</a></li>
    <li><a href='zhangwuji.com'>张无忌</a></li>
    </ul>
"""

# 初始化beautifulSoup对象
page = BeautifulSoup(html, 'html.parser')
result = page.find_all('a')
print(result)
