# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/16 21:30
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import csv
import time

import requests

if __name__ == '__main__':
    with open('./member_list.csv', encoding='utf-8') as fp:
        csv_reader = csv.DictReader(fp)
        for no, item in enumerate(csv_reader):
            avatar_url = item.get('avatarURL').split('?')[0]
            print(no, avatar_url)
            if no < 3280:
                continue
            resp = requests.get(avatar_url, verify=True)
            time.sleep(0.1)
            with open(f"./avatar/{item.get('id')}.jpg", 'wb') as f2:
                f2.write(resp.content)
            # break
