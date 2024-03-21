# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-19 13:16
"""
import execjs
import fake_useragent
import requests

ua = fake_useragent.UserAgent()


def get_x96(tt, tu):
    with open('demo5.js', encoding='utf-8') as fp:
        js_content = fp.read()

    jj = execjs.compile(js_content)
    return jj.call('x93', tt, tu)


session = requests.session()

cookies = {
    '_zap': '29b22fff-b6af-4976-a07c-d25650ac4773',
    'd_c0': 'ADDSD-j4lRePTsK721fRFrWpxQLGjfijbjo=|1697981461',
    'YD00517437729195%3AWM_TID': 'LuLH7LZ%2FK%2BNBBRERVRLFyyI6032kauLu',
    '_xsrf': 'obSsNmCr73VUbekodsFvwlVW1ZxbC69C',
    '__snaker__id': 'OVEO9dZEKxmWl8qP',
    'YD00517437729195%3AWM_NI': 'CIn38fesHw35YIr0Wf7X8RHzTTtsYUWbcv2UFxl%2BWSsYSPTDfAsTBrKnBaBrusQOww517%2FY%2Fz%2FJQOuDjfoizvouLjp3q%2BpYU5X%2B7tpct01AD6GSqjQA6kwgtAw4bgKeeYkM%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee87f780b08fa6d8c95df5bc8fa6c44a968a9b82c462f6f599b0d63d90efa2aff12af0fea7c3b92a8197a2d4bb6ea7ad8898b23f9b97bed1d66ef588f8b3cb72988cbc94dc5f95bead97b15f86a8a4ccd659b1879db1d750a69fbdb5c17a89b28e82c17ab7ad9fb0f67df7eff9d0dc25baf186b2ce7f88b6aa90ec72b6b1bbade97cf1afe591dc5ff788e5d8f77ca1ac00d2c450f6999d92e95b83eaa598e68083a9fc83e641a7bb978cd037e2a3',
    'q_c1': '0389e54222484ac5a1197c8dd8f94c5a|1703592035000|1703592035000',
    'z_c0': '2|1:0|10:1709612766|4:z_c0|80:MS4xN0hnQ0lnQUFBQUFtQUFBQVlBSlZUZnY4ejJZUktrTlczNVhFWDB0R1VmWlZvd05CaHlJRGV3PT0=|6a3445892d129423511b31d7242fdae44243cbb3ed5fd78e7da31dbf9667ca47',
    'tst': 'r',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1709978943,1710499034,1710588805,1710891721',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1711017673',
    'KLBRSID': 'd6f775bb0765885473b0cba3a5fa9c12|1711018325|1711017078',
}

requests.utils.add_dict_to_cookiejar(session.cookies, cookies)

headers = {
    'authority': 'www.zhihu.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': '_zap=29b22fff-b6af-4976-a07c-d25650ac4773; d_c0=ADDSD-j4lRePTsK721fRFrWpxQLGjfijbjo=|1697981461; YD00517437729195%3AWM_TID=LuLH7LZ%2FK%2BNBBRERVRLFyyI6032kauLu; _xsrf=obSsNmCr73VUbekodsFvwlVW1ZxbC69C; __snaker__id=OVEO9dZEKxmWl8qP; YD00517437729195%3AWM_NI=CIn38fesHw35YIr0Wf7X8RHzTTtsYUWbcv2UFxl%2BWSsYSPTDfAsTBrKnBaBrusQOww517%2FY%2Fz%2FJQOuDjfoizvouLjp3q%2BpYU5X%2B7tpct01AD6GSqjQA6kwgtAw4bgKeeYkM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee87f780b08fa6d8c95df5bc8fa6c44a968a9b82c462f6f599b0d63d90efa2aff12af0fea7c3b92a8197a2d4bb6ea7ad8898b23f9b97bed1d66ef588f8b3cb72988cbc94dc5f95bead97b15f86a8a4ccd659b1879db1d750a69fbdb5c17a89b28e82c17ab7ad9fb0f67df7eff9d0dc25baf186b2ce7f88b6aa90ec72b6b1bbade97cf1afe591dc5ff788e5d8f77ca1ac00d2c450f6999d92e95b83eaa598e68083a9fc83e641a7bb978cd037e2a3; q_c1=0389e54222484ac5a1197c8dd8f94c5a|1703592035000|1703592035000; z_c0=2|1:0|10:1709612766|4:z_c0|80:MS4xN0hnQ0lnQUFBQUFtQUFBQVlBSlZUZnY4ejJZUktrTlczNVhFWDB0R1VmWlZvd05CaHlJRGV3PT0=|6a3445892d129423511b31d7242fdae44243cbb3ed5fd78e7da31dbf9667ca47; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1709978943,1710499034,1710588805,1710891721; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1711017673; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1711018325|1711017078',
    'pragma': 'no-cache',
    'referer': 'https://www.zhihu.com/question/616391683/answer/3157488975?utm_psn=1753376002074394624',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ua.random,
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_0QNinW+o2qwzcm2jtQD8wMobKKGaCaOCkV4Pv93X4bCsshYWCM6YnZJyRaJiKeYU',
}

params = {
    'order_by': 'score',
    'limit': '20',
    'offset': '',
}

response = session.get(
    'https://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment',
    params=params,
    cookies=cookies,
    headers=headers,
)

if response.cookies.get_dict():        #保持cookie有效
    session.cookies.update(response.cookies)

result = response.json()
print(result)
print(response.cookies)
for item in result.get('data'):
    print(item.get('author').get('name'), item.get('content'))

next_url = result.get('paging').get('next')
print('下一页:', next_url)

if next_url:
    # print(session.cookies)
    for item in session.cookies:
        print(item)
    # 更新header的 x-zse-96值
    print("cookies['d_co']", cookies.get('d_c0'))
    x96 = get_x96(next_url, cookies.get('d_c0'))
    headers['x-zse-96'] = x96
    print("headers", headers.get('x-zse-96'))
    new_response = session.get(next_url, headers=headers)
    print(new_response.cookies)
    print(new_response.json())
