# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/1 20:32
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import datetime
import json
import random

import requests


def getcapcha_uuid():
    total_string = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
    part = "".join([random.choice(total_string) for _ in range(18)])
    ctime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    captcha_uuid = f"{ctime}{part}"
    return captcha_uuid


def run():
    captchauuid = getcapcha_uuid()

    res = requests.get(
        url='https://captcha1.fengkongcloud.cn/ca/v1/register',
        params={
            "data": {},
            "captchaUuid": captchauuid,
            "organization": "xQsKB7v2qSFLFxnvmjdO",
            "appId": "default",
            "channel": "DEFAULT",
            "lang": "en",
            "model": "slide",
            "callback": "sm_callback",
            "rversion": "1.0.4",
            "sdkver": "1.1.3"
        }
    )
    print(res.text)
    data_dict = json.loads(res.text.strip('sm_callback').strip('(').strip(")"))
    print(data_dict)

if __name__ == '__main__':
    run()