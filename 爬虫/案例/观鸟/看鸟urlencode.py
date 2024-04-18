# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/18 21:42
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from urllib.parse import urlencode, urlparse, parse_qs

data = "page=5&limit=20&taxonid=&startTime=&endTime=&province=%E9%9D%92%E6%B5%B7%E7%9C%81&city=&district=&pointname=&username=&serial_id=&ctime=&taxonname=&state=&mode=0&outside_type=0"
# print(parse_qs(data))
# print(parse_qs(data,keep_blank_values=True))
# print(parse_qs(data, keep_blank_values=True,strict_parsing=True))
params_dict = parse_qs(data, keep_blank_values=True)
params_dict = {k: v[0] for k, v in params_dict.items()}
print(params_dict)
print(urlencode(params_dict))
