# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-21 19:00
"""
# pip install PyExecJS2
import execjs
import requests

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1703029448,1703155799',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1703155799',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1703029448,1703155799; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1703155799',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/since/fake',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'accessToken': '',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
    'v': '231012',
}

params = {
    'isFake': '1',
    'pg': '5',
    'pgsz': '15',
}

response = requests.get(
    'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/project/isFake/all',
    params=params,
    cookies=cookies,
    headers=headers,
).text

print(response)
# 执行js函数
Decrypt_data = execjs.compile(open('./demo2.js','r',encoding='utf-8').read()).call('b',response)
print(Decrypt_data)
