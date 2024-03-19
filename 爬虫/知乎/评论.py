# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-19 13:16
"""
import time

import fake_useragent
import requests

ua = fake_useragent.UserAgent()
cookies = {
    '_zap': '6cc272a9-fab9-48cd-80bf-abff70c21536',
    'd_c0': 'AHBWO4qj1xePTmvvvLzm1-P5ya-H2eLVjLI=|1702388268',
    '_xsrf': 'ilBJqmFgU8UurgfMhq65J4dEu0tegi1I',
    '__snaker__id': '61tnc5jXnp6uo3h0',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1710820695',
    'SESSIONID': 'Y7j6W5CKQIl8e6KEKLplDKox4rqymjIQm4qC2qxojuV',
    'JOID': 'VVgVC0xr-EsCjH9mOGQ_m5I18JUoNc8pO9tNJXs6ticy5kkqfe3itWiLeG4_4fTDVbcN2_6CONFj-CWzob_t-5A=',
    'osd': 'VVgTC05r-E0Cjn9mPmQ9m5Iz8JcoNckpOdtNI3s4tic05ksqfevit2iLfm494fTFVbUN2_iCOtFj_iWxob_r-5I=',
    'l_n_c': '1',
    'l_cap_id': '"ZTVlYjY2ZTQ4MTIxNGQ3OTkxM2MzZGYwOTZkNWNmZTA=|1710822060|a47581e625628480707aa27ce1bd49aa82e49d53"',
    'r_cap_id': '"MDIyNjc4NzkyNjQ0NDY0M2I1ZWRmMmQ4ZjE4ZTc5NWM=|1710822060|601d7a9febcdba76b7ebb6b48307a848df2477ae"',
    'cap_id': '"N2FlYTBkZDMyOWRjNDkwNzlkZDU3NjI1Mzg5MWY1MzE=|1710822060|3dbd5e839b06e6e4ca7fd04ec8f4200db06d5991"',
    'n_c': '1',
    'gdxidpyhxdE': 'WGrCKqXjt3C4OvjhaQb30njeIb80A56DQEsrWEbj6W9p%2B1bDkipy6h%2FZ8PgT%2FrZ7%2FHCt98cKQY%2F8Za16HtwjHinj9afwjVfCX9cshMIL0CN%2B%2Fi%5C0yjn4bt7zddgAbfIB8yz7zI3gSZZH6LnlhUHJAZe8vsG4f3x%5CgIjsYac3oCc%2BMKaW%3A1710825812177',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1710825137',
    'captcha_session_v2': '2|1:0|10:1710825135|18:captcha_session_v2|88:WjFwbERVa0wxcllUYjFqYlBkOGRyQVJWMnhTaTZVV2dlVmdKeXFSZW1uNDd2cDRWYytFNnNFdms4T1BYZ2VMaw==|89208309a9073ee582e818d51f09c75abbfdb85b00249d301ee60943d1038c73',
    'KLBRSID': 'e42bab774ac0012482937540873c03cf|1710825146|1710820686',
}

headers = {
    'authority': 'www.zhihu.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': '_zap=6cc272a9-fab9-48cd-80bf-abff70c21536; d_c0=AHBWO4qj1xePTmvvvLzm1-P5ya-H2eLVjLI=|1702388268; _xsrf=ilBJqmFgU8UurgfMhq65J4dEu0tegi1I; __snaker__id=61tnc5jXnp6uo3h0; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1710820695; SESSIONID=Y7j6W5CKQIl8e6KEKLplDKox4rqymjIQm4qC2qxojuV; JOID=VVgVC0xr-EsCjH9mOGQ_m5I18JUoNc8pO9tNJXs6ticy5kkqfe3itWiLeG4_4fTDVbcN2_6CONFj-CWzob_t-5A=; osd=VVgTC05r-E0Cjn9mPmQ9m5Iz8JcoNckpOdtNI3s4tic05ksqfevit2iLfm494fTFVbUN2_iCOtFj_iWxob_r-5I=; l_n_c=1; l_cap_id="ZTVlYjY2ZTQ4MTIxNGQ3OTkxM2MzZGYwOTZkNWNmZTA=|1710822060|a47581e625628480707aa27ce1bd49aa82e49d53"; r_cap_id="MDIyNjc4NzkyNjQ0NDY0M2I1ZWRmMmQ4ZjE4ZTc5NWM=|1710822060|601d7a9febcdba76b7ebb6b48307a848df2477ae"; cap_id="N2FlYTBkZDMyOWRjNDkwNzlkZDU3NjI1Mzg5MWY1MzE=|1710822060|3dbd5e839b06e6e4ca7fd04ec8f4200db06d5991"; n_c=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1710825209; captcha_session_v2=2|1:0|10:1710825205|18:captcha_session_v2|88:eUdWTENYYVFVVXFMQWdOSm85K21ZcHlpU0R3dllucU5iVW9ySGFKSXpiMGFmVnFkRjFVYkVKcjJ6aFA1VTNyNA==|0d9b8c1e7976ef1f7af29309c0076c660b7bc3d93ca3ec5434dbfdc9b577e43b; gdxidpyhxdE=w6Bxq4OzZWBNsIsx45w7or24VYqQ4tExv%2BPQqCKx2zKsVdU1Throdce5Rzu1B0aNOPShqJV5vGrfClbwnHRVnse%2FT3Bbv2joEbzQyBqXo8zbOvjlyWEL%2By6zvZRr7GbN%2B8gYzzyqtVxAnLyt2Q31%2ByH5onAkQP7O8EiXQ4UBDUV4Mq%2Bn%3A1710843339841; KLBRSID=d1f07ca9b929274b65d830a00cbd719a|1710842467|1710842435',
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
    'x-zse-96': '2.0_veDZfSyz90Ja4xqjZynrcXWnSyk0mXwJP7dtpDaRiQr=ne3=sxsLD7tzvcnojx',
}

params = {
    'order_by': 'score',
    'limit': '20',
    'offset': '',
}

session = requests.session()
requests.utils.add_dict_to_cookiejar(session.cookies, cookies)

response = session.get(
    'https://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment',
    params=params,
    cookies=cookies,
    headers=headers,
)

result = response.json()
print(result)
print(response.cookies)
for item in result.get('data'):
    print(item.get('author').get('name'), item.get('content'))

next_url = result.get('paging').get('next')
print(next_url)
time.sleep(1)
print(ua.edge)
headers.update({'user-agent': ua.edge,
                'referer':'https://www.zhihu.com/question/616391683/answer/2111409251'})
print(headers)
if next_url:
    new_response = session.get(next_url, headers=headers, cookies=response.cookies)
    print(new_response.cookies)
    print(new_response.json())
