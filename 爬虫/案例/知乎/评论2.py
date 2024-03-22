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
    with open('zhihu_x-zse-96.js', encoding='utf-8') as fp:
        content = fp.read()
        jj = execjs.compile(content)

        return jj.call('get_xzse96', d_c0, url)


session = requests.session()

cookies = {
    '_zap': '3ac25dde-c84d-4d65-bf3b-c9a16dadabfd',
    'd_c0': '"AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521"',
    'gdxidpyhxdE': 'n4NdX46ypEdknH4e%2FvI%2BrC%2BUe%2FgxoIe%5CXEuGVu%5CnxZ80R%5CmUNVlkrjBWNBWikhDrTJZ3uYvAeKbLSaerWI0q3%5CKnhJYUGP5JPIq9xlHqdWdSNb8GyG3b4oJ%2Fo3E8TLsXCNqhfz2U62PQ4dEVB28iRjYn%2BSznqkLAPoc0xvE7z1G6NB4I%3A1710861951154',
    '_xsrf': 'c244a1d1-d54e-428c-80e7-7e8f5f71d1e3',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1710772602,1710851457,1710940856,1711030594',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1711030594',
    'captcha_session_v2': '2|1:0|10:1711030594|18:captcha_session_v2|88:dUx2NGZyeGlteXFpYzNudHJlWE9waEVqV2pvdDVWcjlEQ2N6cXFWTkc5ZC8rbkZSL01GUFJBS0xHMEJUamcrQw==|e28a0fe9493257052d3502b5e4f80ac25c014267f0dd1c32982bfec9b84a0ef9',
    'KLBRSID': 'c450def82e5863a200934bb67541d696|1711030604|1711030590',
}

headers = {
    'authority': 'www.zhihu.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': '_zap=3ac25dde-c84d-4d65-bf3b-c9a16dadabfd; d_c0="AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521"; gdxidpyhxdE=n4NdX46ypEdknH4e%2FvI%2BrC%2BUe%2FgxoIe%5CXEuGVu%5CnxZ80R%5CmUNVlkrjBWNBWikhDrTJZ3uYvAeKbLSaerWI0q3%5CKnhJYUGP5JPIq9xlHqdWdSNb8GyG3b4oJ%2Fo3E8TLsXCNqhfz2U62PQ4dEVB28iRjYn%2BSznqkLAPoc0xvE7z1G6NB4I%3A1710861951154; _xsrf=c244a1d1-d54e-428c-80e7-7e8f5f71d1e3; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1710772602,1710851457,1710940856,1711030594; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1711030594; captcha_session_v2=2|1:0|10:1711030594|18:captcha_session_v2|88:dUx2NGZyeGlteXFpYzNudHJlWE9waEVqV2pvdDVWcjlEQ2N6cXFWTkc5ZC8rbkZSL01GUFJBS0xHMEJUamcrQw==|e28a0fe9493257052d3502b5e4f80ac25c014267f0dd1c32982bfec9b84a0ef9; KLBRSID=c450def82e5863a200934bb67541d696|1711030604|1711030590',
    'pragma': 'no-cache',
    'referer': 'https://www.zhihu.com/question/616391683/answer/3157488975?utm_psn=1753376002074394624',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_0LyqV/iOX=V+XL/VQ5D0e1Meq=DxP+VZA6kNJcKhprnHsIZlBvTMPuqDBtaQpgTQ',
}

params = {
    'order_by': 'score',
    'limit': '20',
    'offset': '',
}

url = 'https://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment'

response = session.get(url,
                       params=params,
                       cookies=cookies,
                       headers=headers,
                       )

result = response.json()

pprint.pprint(result)

next_url = result.get('paging').get('next')

for cookie in session.cookies:
    print(f"{cookie.name} = {cookie.value}")

if next_url:
    print(next_url)
    print('cookie.get(d_c0)', cookies.get('d_c0'))
    x96 = get_x96(cookies.get('d_c0'), next_url)
    print(x96)
    headers['x-zse-96'] = '2.0_hM5CzP5jfO65xXAuZpa3QfF0kXe/=c5daGkzi99xS3sLx9S1iDr290KczYKSBCmW'

    print(session.get(next_url, headers=headers).json())
