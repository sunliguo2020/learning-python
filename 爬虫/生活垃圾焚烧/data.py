# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-25 22:15
"""
import pandas as pd
import requests

url = 'https://ljgk.envsc.cn/OutInterface/GetPSList.ashx?regionCode=0&psname=&SystemType=C16A882D480E678F&sgn=02deea4e16bf7b646e2aac3202d8330e6f2b95a5&ts=1703513263347&tc=59487241'
resp = requests.get(url).json()

# 将字典列表转换为DataFrame对象
df = pd.DataFrame(resp)

# 将DataFrame写入Excel文件
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
