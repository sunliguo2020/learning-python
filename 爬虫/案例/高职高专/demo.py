# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/3 16:07
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

cookies = {
    'BIGipServerswww_pool': '738328842.20480.0000',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=utf-8',
    # 'Cookie': 'BIGipServerswww_pool=738328842.20480.0000',
    'Pragma': 'no-cache',
    'Referer': 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_73_11/tj/tjkl.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_73_11/data/tjkl.json',
                        # cookies=cookies,
                        headers=headers)

print(response.json())