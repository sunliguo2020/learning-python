# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/1 20:03
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import datetime
import random
import time

import requests

total_string = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
part = "".join([random.choice(total_string) for _ in range(18)])
ctime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
captcha_uuid = f"{ctime}{part}"

res = requests.get(
    url='https://captcha1.fengkongcloud.cn/ca/v1/conf',
    params={
        'captchaUuid': captcha_uuid,
        'model': 'select',
        'appId': 'default',
        'rversion': '1.0.4',
        'sdkver': '1.1.3',
        'callback': f"sm_{int(time.time())}",
        "organization": 'xQsKB7v2qSFLFxnvmjdO',

        "channel": 'DEFAULT',
        "lang": "zh-cn"
    }
)

print(res.text)