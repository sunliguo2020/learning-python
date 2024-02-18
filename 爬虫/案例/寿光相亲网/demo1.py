# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/15 22:13
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import datetime
import pprint

import requests
from hashtoken import r_hashtoken

# 时间戳
timestamp = str(datetime.datetime.now().timestamp() * 1000)
# print(timestamp)
hashtoken = r_hashtoken(timestamp)
# print(hashtoken)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.sgjhw.com/web/member/1186282',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'hashtoken': hashtoken,
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'actiontype': 'member',
    'id': '414530',
}

response = requests.get('https://www.sgjhw.com/pc/love/getObjectProfile', params=params, headers=headers)

pprint.pprint(response.json())
