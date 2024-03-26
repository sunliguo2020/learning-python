# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-23 18:50
"""
import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://ygp.gdzwfw.gov.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "X-Dgi-Req-App": "ggzy-portal",
    "X-Dgi-Req-Nonce": "w6M8RJCZq4v10jG9",
    "X-Dgi-Req-Signature": "0b915e37868bbc65384e00d4e8e0c8408bdb95c24829645966df10f65b0d766c",
    "X-Dgi-Req-Timestamp": "1711190927641",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "_horizon_sid": "f9159f7f-c434-49ce-9085-d2a79ab26172",
    "_horizon_uid": "6834b27e-f384-4c19-96da-9e5b352cd7df"
}
url = "https://ygp.gdzwfw.gov.cn/ggzy-portal/center/apis/trading-notice/new/detail"
params = {
    "nodeId": "1769639428744863750",
    "version": "v3",
    "tradingType": "A",
    "noticeId": "f0fdd9b7-6b95-4888-bcd3-9337312bf0c7",
    "bizCode": "3C51",
    "projectCode": "E4401000002400711001",
    "siteCode": "440100"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)