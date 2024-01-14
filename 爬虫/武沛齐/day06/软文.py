# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-13 18:21
"""
import ddddocr
import requests

res = requests.post('https://api.ruanwen.la/api/auth/captcha/generate')
res_dict = res.json()

captcha_token = res_dict.get('data').get('captcha_token')
pic_src = res.json().get('data').get('src')

res = requests.get(url=pic_src)
# print(res.content)
with open('xx.png', 'wb') as fp:
    fp.write(res.content)

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)

cookies = {
    'utm_fv': 'https://i.ruanwen.la/',
    'pid': 'eyJpdiI6IkZCOXhiNE9mSE55N09HWFwvUTZCU1dRPT0iLCJ2YWx1ZSI6IlpmVTBkam5SRHh5VVcwbERDOXV2R1E9PSIsIm1hYyI6ImQ0M2VmYzhmMDBmZmQ2YzRmNzJkYWY5ZWViM2JmNDVhYThkZWRiZTViZDQ4ZjgyMmJkZmQ2YzZhMjAzOTMxZmMifQ%3D%3D',
    'XSRF-TOKEN': 'eyJpdiI6IlRKNmF3K1h4bm1yV3pNVEFyd25pa3c9PSIsInZhbHVlIjoia21PSnJ3WUZyTzREVE5wSE5ZTWVvXC9IXC9jc3FKbDFGUXpTZjhseTFqVlQ2RzBaY1wvenNEM3FPZVdtU1wveWhkNU8iLCJtYWMiOiI2YzAwZDBkN2EzNjdiZGRkNTgxZDIyOTRkNmQ2N2U3YjI1OGJlMDUzMDM0YTU4NmZmZGU5MjdiZTMxMDBlZWJmIn0%3D',
    'SESSION_COOKIE': 'eyJpdiI6Imk5ZFNaZnVKN05BVHgySmdlRkpFSEE9PSIsInZhbHVlIjoiZTVDZ2NUY3dlMllpWnI3RDFQNFRtRCsxc1dyVHg3aUJvXC9SODY3Y2hzWkZQREVLNmNBUU81WDVCXC9Jdk1POEVwIiwibWFjIjoiMDcyMTljY2RkNDJmMzllZWExZGFhOTQzNjBmNzQ1MmVhZTRiN2QzZWVmOTRjYmM2YWM0MTdkYzZhYmVhZWU3YSJ9',
}

headers = {
    'authority': 'api.ruanwen.la',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'utm_fv=https://i.ruanwen.la/; pid=eyJpdiI6IkZCOXhiNE9mSE55N09HWFwvUTZCU1dRPT0iLCJ2YWx1ZSI6IlpmVTBkam5SRHh5VVcwbERDOXV2R1E9PSIsIm1hYyI6ImQ0M2VmYzhmMDBmZmQ2YzRmNzJkYWY5ZWViM2JmNDVhYThkZWRiZTViZDQ4ZjgyMmJkZmQ2YzZhMjAzOTMxZmMifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IlRKNmF3K1h4bm1yV3pNVEFyd25pa3c9PSIsInZhbHVlIjoia21PSnJ3WUZyTzREVE5wSE5ZTWVvXC9IXC9jc3FKbDFGUXpTZjhseTFqVlQ2RzBaY1wvenNEM3FPZVdtU1wveWhkNU8iLCJtYWMiOiI2YzAwZDBkN2EzNjdiZGRkNTgxZDIyOTRkNmQ2N2U3YjI1OGJlMDUzMDM0YTU4NmZmZGU5MjdiZTMxMDBlZWJmIn0%3D; SESSION_COOKIE=eyJpdiI6Imk5ZFNaZnVKN05BVHgySmdlRkpFSEE9PSIsInZhbHVlIjoiZTVDZ2NUY3dlMllpWnI3RDFQNFRtRCsxc1dyVHg3aUJvXC9SODY3Y2hzWkZQREVLNmNBUU81WDVCXC9Jdk1POEVwIiwibWFjIjoiMDcyMTljY2RkNDJmMzllZWExZGFhOTQzNjBmNzQ1MmVhZTRiN2QzZWVmOTRjYmM2YWM0MTdkYzZhYmVhZWU3YSJ9',
    'origin': 'https://i.ruanwen.la',
    'platform': 'xinmeibao',
    'referer': 'https://i.ruanwen.la/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-identity': 'advertiser',
}

json_data = {
    'mobile': '2323232',
    'device': 'pc',
    'password': '23232',
    'captcha_token': captcha_token,
    'captcha': code,
    'identity': 'advertiser',
}

response = requests.post('https://api.ruanwen.la/api/auth/authenticate', cookies=cookies, headers=headers,
                         json=json_data)

print(response.json())