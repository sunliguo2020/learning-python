# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/24 17:04
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from playwright.sync_api import sync_playwright
import time
import requests

import requests

headers = {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.zhihu.com/question/616391683/answer/3157488975?utm_psn=1753376002074394624",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": "2.0_MLR2FKHfwjG3xKjUsc=jjDtAee4MkcYP00U4yqFMnAdWZcq43TBxvu5hiNC9O7iT"
}
cookies = {
    "_zap": "3ac25dde-c84d-4d65-bf3b-c9a16dadabfd",
    "d_c0": "\"AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521\"",
    "_xsrf": "f215dd31-3380-4893-885a-03674539708e",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1710940856,1711030594,1711202531,1711249708",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1711270927",
    "captcha_session_v2": "2|1:0|10:1711270929|18:captcha_session_v2|88:L3VkK3BzdG5qSWhCRktYVWIrTnZzMTNidld2QXhnSW02SWMwRjkxTGlITGQzVFRWa3hKZXJaUHQzOTZzWHlIRQ==|33787d6de4c66d40ac99898811020d22b8804abe3bc6d5109c60f6f82d77d3d2",
    "gdxidpyhxdE": "zYPgKATT54bNu6jh4vX%2F0pnoMlPB206DngYD1mBZ0486cfm622Ydox9Erj9mwwNy0RM1Zzj3kjUR%2BzdOa0UW5uBXzqU6SzU%2FoyDRnPWPyQexbZt0R%5CMCo9aXYOQqBnEvv%2F3MVd3UOJma2I7tc27sA%5CwAh%2BJcWajna%2BwYmKqhPpSyq78m%3A1711271871198",
    "KLBRSID": "c450def82e5863a200934bb67541d696|1711271070|1711270924"
}
url = "https://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment"
params = {
    "order_by": "score",
    "limit": "20",
    "offset": ""
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.json())

BASE_URL = 'https://static.zhihu.com/heifetz/1814.app.2d0e908f2b43f21d9681.js'

context = sync_playwright().start()
browser = context.chromium.launch(headless=False)
page = browser.new_page()
page.route(
    "**/1814.app.2d0e908f2b43f21d9681.js",
    lambda route: route.fulfill(path="./chunk.js")
)
page.goto(BASE_URL)


def get_x96(tt):
    print('tt', tt)
    tr = {
        "zse93": "101_3_3.0",
        "dc0": "\"AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521\"",
        "xZst81": ''
    }

    # result = page.evaluate('''() => {
    #         return window.encrypt("%s", "%s", "%s", "%s")
    #     }''' % (tt, 'undefined', tr, 'undefined'))
    # return result

    # result = page.evaluate(f"()=>{{ return window.encrypt({tt},{'undefined'},{tr},{'undefined'})}}")
    result = page.evaluate(f"()=>{{ return window.encrypt2}}")
    return result


print(get_x96('https://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment'))
time.sleep(1000)
