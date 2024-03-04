# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/3 13:37
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

from hashtoken import header_hashtoken

hashtoken_data = header_hashtoken()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.sgjhw.com/web/case/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'hashtoken': hashtoken_data,
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'actiontype': 'tuodan',
    'page': '1',
}

response = requests.get('https://www.sgjhw.com/pc/love/tuodan', params=params, headers=headers)
print(response.json()['data']['list'][0])
