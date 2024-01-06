# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-05 19:31
"""
import requests

from demo1 import encrypt

cookies = {
    'BSFIT_kwjmB': '',
    'route': 'ef535e3a0d0b78922cdc0df3d6b94403',
    'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2': '1704366993,1704453001',
    'BSFIT_EXPIRATION': '1704525287165',
    'BSFIT_DEVICEID': 'eKCPbJ4Sow8J93yAdDbyT3zxK1XKESdHvyC-HrFd9PMqJzxDeAM0MWLP78Zh05Si3uIO5kBi1sSZ552OCDs7yg9LYjO1EGFett0naxU3A2MkOVfoAHrGVIQ3KLPSkDLJ56rd_SLGSZYx6bxlXTRbJWphZ--7tOtO',
    'Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2': '1704453696',
    '__ts': '1704453695000',
    'BSFIT_iv7m8': 'zCRH+m21+m8y+M8HzH,zmiVum3HzmzMzH',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'BSFIT_kwjmB=; route=ef535e3a0d0b78922cdc0df3d6b94403; Hm_lvt_b966fe201514832da03dcf6cbf25b8a2=1704366993,1704453001; BSFIT_EXPIRATION=1704525287165; BSFIT_DEVICEID=eKCPbJ4Sow8J93yAdDbyT3zxK1XKESdHvyC-HrFd9PMqJzxDeAM0MWLP78Zh05Si3uIO5kBi1sSZ552OCDs7yg9LYjO1EGFett0naxU3A2MkOVfoAHrGVIQ3KLPSkDLJ56rd_SLGSZYx6bxlXTRbJWphZ--7tOtO; Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2=1704453696; __ts=1704453695000; BSFIT_iv7m8=zCRH+m21+m8y+M8HzH,zmiVum3HzmzMzH',
    'Origin': 'https://ctbpsp.com',
    'Referer': 'https://ctbpsp.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'keyword': '山东佳辰灵通信息技术有限公司',
    'uid': '0',
    'PageSize': '10',
    'CurrentPage': '1',
    'searchType': '0',
    'bulletinType': '5',
}

response = requests.post('https://ctbpsp.com/cutominfoapi/searchkeyword', params=params, cookies=cookies,
                         headers=headers, verify=False)
print(encrypt(response.text))
