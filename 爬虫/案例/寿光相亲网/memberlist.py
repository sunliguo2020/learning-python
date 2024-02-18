# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/16 19:05
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import csv
import datetime
import json

import requests
from hashtoken import r_hashtoken

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.sgjhw.com/web/member/list',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'hashtoken': r_hashtoken(str(datetime.datetime.now().timestamp() * 1000)),
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_member_list(page):
    params = {
        'actiontype': 'member',
        'page': page,
        'is_count': '0',
    }
    member_list_url = 'https://www.sgjhw.com/pc/love/listrecommend'
    response = requests.get(member_list_url, params=params, headers=headers)

    # print(response.json())
    return response


if __name__ == '__main__':
    member_list = []
    for page in range(1, 213):
        print(page)
        resp = get_member_list(page)
        # resp.encoding = 'utf-8'
        # print(json.dumps(resp.json()))

        resp_json = resp.json().get('data').get('list')
        member_list.extend(resp_json)

        # 加上参数ensure_ascii 避免中文显示为ascii
        json_str = json.dumps(resp_json, ensure_ascii=False)

        with open(f"./json/{page}.json", mode='w', encoding='utf-8') as fp:
            # fp.write(resp.content.decode("unicode-escape"))
            # json.dump(obj=resp.json(), fp=fp)
            fp.write(json_str)

    with open(f'member_list.csv', 'w', newline='', encoding='utf-8') as f2:
        csv_writer = csv.DictWriter(f2, fieldnames=resp_json[0].keys())
        csv_writer.writeheader()
        for item in member_list:
            csv_writer.writerow(item)
