# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-08-10 21:07
"""
import urllib.request
url = 'https://ke.qq.com/webcourse/3488810/105769972#taid=14352694079994922&live=1'
print(urllib.request.unquote(url))
print(urllib.request.quote('迪丽热巴'))