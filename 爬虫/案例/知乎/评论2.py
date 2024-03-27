# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/21 22:18
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import pprint

import execjs
import requests


def get_x96(d_c0, url):
    # print('get_x96',url)
    with open('demo5.js', encoding='utf-8') as fp:
        content = fp.read()
        jj = execjs.compile(content)

        return jj.call('x96', url, d_c0)


cookies = {
    '_zap': '3ac25dde-c84d-4d65-bf3b-c9a16dadabfd',
    'd_c0': '"AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521"',
    '_xsrf': '6397c23f-4da5-4665-a74b-9deeb0b2fc65',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1711249708,1711373696,1711379050,1711454950',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1711457442',
    'captcha_session_v2': '2|1:0|10:1711457443|18:captcha_session_v2|88:bCtXVWh6YnJjRTV2RWxNRGh0a0Ewd0dtcE1HQzhFa2o5ZHBQNmlhclIreE5LWE92VXdCcjhGd2tEaC9zSzV6dw==|ab9af4fdc3abffb027da859175d85fc54d709da65229ba6120e04a35cd941266',
    'gdxidpyhxdE': 'phCVqSY4nGCvm218SG0h%2FfLJM6eXCQOOsDOYK%2FW4IbYCOd05uw3jVXTQlaH6lTig%5CwerDQXzH0bO2X%2FY%2FKa2KCLtk0th%5CacY%2BGXN79G0Ilwv%5CfgGoKJBL7vUgm%5C7uddG0nX8YZ%5CEvP9XCNAPne%5C4gXL3i80Q%2B1gM08cUTJNoeLh%2BBjzy%3A1711458347976',
    'KLBRSID': 'dc02df4a8178e8c4dfd0a3c8cbd8c726|1711457734|1711454951',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': '_zap=3ac25dde-c84d-4d65-bf3b-c9a16dadabfd; d_c0="AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521"; _xsrf=6397c23f-4da5-4665-a74b-9deeb0b2fc65; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1711249708,1711373696,1711379050,1711454950; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1711457442; captcha_session_v2=2|1:0|10:1711457443|18:captcha_session_v2|88:bCtXVWh6YnJjRTV2RWxNRGh0a0Ewd0dtcE1HQzhFa2o5ZHBQNmlhclIreE5LWE92VXdCcjhGd2tEaC9zSzV6dw==|ab9af4fdc3abffb027da859175d85fc54d709da65229ba6120e04a35cd941266; gdxidpyhxdE=phCVqSY4nGCvm218SG0h%2FfLJM6eXCQOOsDOYK%2FW4IbYCOd05uw3jVXTQlaH6lTig%5CwerDQXzH0bO2X%2FY%2FKa2KCLtk0th%5CacY%2BGXN79G0Ilwv%5CfgGoKJBL7vUgm%5C7uddG0nX8YZ%5CEvP9XCNAPne%5C4gXL3i80Q%2B1gM08cUTJNoeLh%2BBjzy%3A1711458347976; KLBRSID=dc02df4a8178e8c4dfd0a3c8cbd8c726|1711457734|1711454951',
    'pragma': 'no-cache',
    'referer': 'https://www.zhihu.com/question/616391683/answer/3157488975?utm_psn=1753376002074394624',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_Su7ic8HAXSLUR0uVLFRj/ezoUvWrkxD=S6HA8AbBXxvIMKLT3h23u5NjqoGSoaKb',
}

params = {
    'order_by': 'score',
    'limit': '20',
    'offset': '5_10644383414_0',
}

response = requests.get(
    'https://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment',
    params=params,
    cookies=cookies,
    headers=headers,
)

result = response.json()

# pprint.pprint(result)

next_url = result.get('paging').get('next')

# for cookie in session.cookies:
#     print(f"{cookie.name} = {cookie.value}")

if next_url:
    print(next_url)
    print('cookie.get(d_c0)', cookies.get('d_c0'))
    x96 = get_x96(cookies.get('d_c0'), next_url)
    print(x96)
    headers['x-zse-96'] = x96
    print(requests.get(next_url, headers=headers).json())
