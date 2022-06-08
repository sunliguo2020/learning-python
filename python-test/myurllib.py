# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/3/15 9:41
"""

import urllib.request
response = urllib.request.urlopen("http://www.baidu.com",data=byte("sd",'urt-8'))
print(response.read().decode('utf-8'))