# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/17 12:30
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://turing.captcha.gtimg.com/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://turing.captcha.qcloud.com/cap_union_new_getcapbysig?img_index=1&image=027905000000003500000009dcda2ead39fe&sess=s0SVrVcxeEXETHYh0a78Zvw5EABuawUp4tgLGZo3Be89whKaY6VGUG1s-CfxHv-1MwWSHQnwS4Gf69PA-mNtM2aw9qGOGdoVRJhq_oGBGwR0LtVNIGyi-2bmqP7T_vvWbhze7tWLVyOI8SsVplyjr4607HQ2fACGMiln1kPEmxcCvTiGJzXKw2mjz7Ykuad1e35jEV5gUJR0-NAMJLa6uQZ4dH6pRtFUOjYo_-IBb2AUnKc-i_0IgLwKqpWCSoHivChDWLAIFwFNjakaP_GmxAcHahHzbAHf8gcXxNQt0BfhNfDlPgmqJVVUx11Cn0cg0rY95b5t3JJXHSKtvT4jLr60b8JuemDhmp3psTdsuzjZhphFjvqtq_r8ObRhPZAfU_gPLPWTPGUTHRczxHfLC-YphK403cRAl3aA1MH-0ouMg*',
    headers=headers,
)
print(response.content)

with open('bg.jpg', 'wb') as fp:
    fp.write(response.content)
