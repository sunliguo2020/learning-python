# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-02 13:12
获取网易云音乐评论
"""
import execjs
import requests

cookies = {
    'NMTID': '00O9GLzozva10lck0DDiZ0QvbzLk9UAAAGMtfzcjw',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': 'c35a4bc4fd8cbbeafdef8f3f8dc19ea3,1703860300163',
    '_ntes_nuid': 'c35a4bc4fd8cbbeafdef8f3f8dc19ea3',
    'WM_TID': '2r6TVUCFUqxBQURUEFPQsYsnv%2BX%2FR2cg',
    'WEVNSM': '1.0.0',
    'WNMCID': 'gqycaj.1703860304040.01.0',
    'sDeviceId': 'YD-Q7eYEqkF3wFBUgUVVEaV9M5m%2FvZS29Nt',
    'ntes_utid': 'tid._.baz2wegv5HRAQwQQABOBtN4y%252B6MCptgh._.0',
    'JSESSIONID-WYYY': 'pRl0%2FciUODHT5tFJeH6ZmmSHgYG%5CsifKAgtNynda9XCOJTWWqIWuWi8KF5yFgA0JuwtaAmgUApWY%2F%5CTmy30sxB8tRoauIYppt9cn002dPMk%2Boqjsj9t8%5C%5CN1vJrW9eHQV4l5K%2F%2FNH%2FZ%2BS%5C5R%2B0vd97V20rHpcD6cdwAHUu5P2MuIaT3P%3A1704173891629',
    'WM_NI': 'l1P8%2FEcZjf9rpqQjo0Md89L5PjY8SCNEMC4y2jJ0VEsnS9CaNEExxv7dvZUTj9idcRd%2B0JWdsJPleeaSW8XL1a9U3XYaZ5a2iEYT8IR3FaNghtBWg1Uppyj9stx5T9g1SUE%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eea6b56388eebc89b863ac8e8fb7c55f939a8a82c43390998ad2fb72f29700a6ed2af0fea7c3b92ab0efa0d9ae4fa186a687bc7ab4af9f8bee3c8fbcf8dacf3f94b697d9d2498e9b83a4b773f2b686d1d54fb1b29ddac26b8e9b8b99fb7ef5bcbabbd860aae7a785e25aa8f500abd670b196a08de86fa38d99d9db48f3bff7b6b2549bbf96d6e43aab9b97b5bb4392ed8a82cd6dacac8eb8e63b97b0c09ae933b1acb8d6d733a5ef9db6c837e2a3',
}

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'NMTID=00O9GLzozva10lck0DDiZ0QvbzLk9UAAAGMtfzcjw; _iuqxldmzr_=32; _ntes_nnid=c35a4bc4fd8cbbeafdef8f3f8dc19ea3,1703860300163; _ntes_nuid=c35a4bc4fd8cbbeafdef8f3f8dc19ea3; WM_TID=2r6TVUCFUqxBQURUEFPQsYsnv%2BX%2FR2cg; WEVNSM=1.0.0; WNMCID=gqycaj.1703860304040.01.0; sDeviceId=YD-Q7eYEqkF3wFBUgUVVEaV9M5m%2FvZS29Nt; ntes_utid=tid._.baz2wegv5HRAQwQQABOBtN4y%252B6MCptgh._.0; JSESSIONID-WYYY=pRl0%2FciUODHT5tFJeH6ZmmSHgYG%5CsifKAgtNynda9XCOJTWWqIWuWi8KF5yFgA0JuwtaAmgUApWY%2F%5CTmy30sxB8tRoauIYppt9cn002dPMk%2Boqjsj9t8%5C%5CN1vJrW9eHQV4l5K%2F%2FNH%2FZ%2BS%5C5R%2B0vd97V20rHpcD6cdwAHUu5P2MuIaT3P%3A1704173891629; WM_NI=l1P8%2FEcZjf9rpqQjo0Md89L5PjY8SCNEMC4y2jJ0VEsnS9CaNEExxv7dvZUTj9idcRd%2B0JWdsJPleeaSW8XL1a9U3XYaZ5a2iEYT8IR3FaNghtBWg1Uppyj9stx5T9g1SUE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea6b56388eebc89b863ac8e8fb7c55f939a8a82c43390998ad2fb72f29700a6ed2af0fea7c3b92ab0efa0d9ae4fa186a687bc7ab4af9f8bee3c8fbcf8dacf3f94b697d9d2498e9b83a4b773f2b686d1d54fb1b29ddac26b8e9b8b99fb7ef5bcbabbd860aae7a785e25aa8f500abd670b196a08de86fa38d99d9db48f3bff7b6b2549bbf96d6e43aab9b97b5bb4392ed8a82cd6dacac8eb8e63b97b0c09ae933b1acb8d6d733a5ef9db6c837e2a3',
    'nm-gcore-status': '1',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/song?id=1325905146',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': '',
}

data = {
    "csrf_token": "",
    "cursor": "1704203771403",
    "offset": "0",
    "orderType": "1",
    "pageNo": "2",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}
import json

json_dump = json.dumps(data)
# print(json_dump)

js = execjs.compile(open('网易.js','r',encoding='utf-8').read())
result = js.call("fn",json_dump)
# print(result)
# 准备数据

real_data = {
    'params': result.get('encText'),
    'encSecKey': result.get('encSecKey'),
}

response = requests.post(
    'https://music.163.com/weapi/comment/resource/comments/get',
    headers=headers,
    data=real_data,
)
print(response.content.decode('utf-8'))
