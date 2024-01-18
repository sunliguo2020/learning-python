# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/17 23:27
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 滑动请求.py
 @Project : learning-python
"""
import requests
import execjs

with open('模拟轨迹.js', 'r', encoding='utf-8') as fp:
    js = fp.read()

JS = execjs.compile(js)

data = JS.call('func')
print(data)
cookies = {
    'QN1': '0000ea80306c5af20058a1eb',
    'QN300': 'organic',
    'QN99': '9350',
    'qunar-assist': '{%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}',
    'QN205': 'organic',
    'QN277': 'organic',
    'QN267': '03637566343afa4256',
    'csrfToken': 'z7Zsz3bI6wBkDj1V2S8tLvWZa8I7uneP',
    'QunarGlobal': '10.72.48.24_-7e14ca11_18d1673d5ca_6c40|1705490956232',
    '_i': 'ueHd8ZkXXXVXqeqA-RUsWm9c0kRX',
    '_vi': 'psUbBjblLcId_fWdX7ylzJuOtEDzH9PdkQ9aHMJLYRlovzL6eyVXk3Ve6Sj1pvttSD029sHZkpE0W0ffNRbESmN0dByEa9d7vPI1vm3_670kzrlPsH5NQ_RJRCUrbBInuzQZGYH8vuQNvqVdBO_ZyL0xyULCTTOw9Lch-6N-AYr_',
    'QN269': 'A5BE08E1B52B11EE82829EDE1915F0C4',
    'QN601': '6db340d059de52e6dcc8f4ee08fc004f',
    'QN48': '0000f5802f105af200600bcb',
    'QN163': '0',
    'fid': 'e015c9ee-f271-409b-8d24-1be75cd1b552',
    'QN271': 'a7821061-791a-4ea0-a615-b99659c5e2fd',
    'ctt_june': '1683616182042##iK3wWRawWUPwawPwa%3Dj%3DaSP%2BED3%3DESgnERj%2BaP3wVPaAaPXNWRiTER3nWRt%2BiK3siK3saKg8WKXNaR2AVKP%2BWUPwaUvt',
    'QN271AC': 'register_pc',
    'QN271SL': '5b6cf3eb42bac8fde90c6a214a53272a',
    'QN271RC': '5b6cf3eb42bac8fde90c6a214a53272a',
    'ariaDefaultTheme': 'undefined',
    'ctf_june': '1683616182042##iK3wWS3%3DWhPwawPwasDsWKjmasPNVP3sEKDAWDanED3%2BaRHTX%3D3%2BaKEIX%3DiDiK3siK3saKg8WKP8asDmWstsWuPwaUvt',
    'cs_june': 'e389ff45f9ae4b8288f72ab92e8503891e1aaf8f4fdb65382854cf72624490cdf746750334d6f023c8722f6765aa464cbe3e27be81c12e4d339099d1734c7ef2b17c80df7eee7c02a9c1a6a5b97c1179005cd82922e5932131456d9b75bc01985a737ae180251ef5be23400b098dd8ca',
}

headers = {
    'authority': 'vercode.qunar.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'content-type': 'text/plain;charset=UTF-8',
    # 'cookie': 'QN1=0000ea80306c5af20058a1eb; QN300=organic; QN99=9350; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN205=organic; QN277=organic; QN267=03637566343afa4256; csrfToken=z7Zsz3bI6wBkDj1V2S8tLvWZa8I7uneP; QunarGlobal=10.72.48.24_-7e14ca11_18d1673d5ca_6c40|1705490956232; _i=ueHd8ZkXXXVXqeqA-RUsWm9c0kRX; _vi=psUbBjblLcId_fWdX7ylzJuOtEDzH9PdkQ9aHMJLYRlovzL6eyVXk3Ve6Sj1pvttSD029sHZkpE0W0ffNRbESmN0dByEa9d7vPI1vm3_670kzrlPsH5NQ_RJRCUrbBInuzQZGYH8vuQNvqVdBO_ZyL0xyULCTTOw9Lch-6N-AYr_; QN269=A5BE08E1B52B11EE82829EDE1915F0C4; QN601=6db340d059de52e6dcc8f4ee08fc004f; QN48=0000f5802f105af200600bcb; QN163=0; fid=e015c9ee-f271-409b-8d24-1be75cd1b552; QN271=a7821061-791a-4ea0-a615-b99659c5e2fd; ctt_june=1683616182042##iK3wWRawWUPwawPwa%3Dj%3DaSP%2BED3%3DESgnERj%2BaP3wVPaAaPXNWRiTER3nWRt%2BiK3siK3saKg8WKXNaR2AVKP%2BWUPwaUvt; QN271AC=register_pc; QN271SL=5b6cf3eb42bac8fde90c6a214a53272a; QN271RC=5b6cf3eb42bac8fde90c6a214a53272a; ariaDefaultTheme=undefined; ctf_june=1683616182042##iK3wWS3%3DWhPwawPwasDsWKjmasPNVP3sEKDAWDanED3%2BaRHTX%3D3%2BaKEIX%3DiDiK3siK3saKg8WKP8asDmWstsWuPwaUvt; cs_june=e389ff45f9ae4b8288f72ab92e8503891e1aaf8f4fdb65382854cf72624490cdf746750334d6f023c8722f6765aa464cbe3e27be81c12e4d339099d1734c7ef2b17c80df7eee7c02a9c1a6a5b97c1179005cd82922e5932131456d9b75bc01985a737ae180251ef5be23400b098dd8ca',
    'origin': 'https://user.qunar.com',
    'referer': 'https://user.qunar.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

data = {
    "data": data,
    "orca": 2,
    "appCode":
        "register_pc",
    "cs": "pc"}

response = requests.post('https://vercode.qunar.com/inner/captcha/snapshot',
                         # cookies=cookies,
                         headers=headers,
                         json=data)
print(response.text)

# # {"ret":true,"errCode":0,"errMsg":null,"data":{"code":0,"timestamp":1705505389965,"cst":"d932156ad23bb851d5e72bd49d34ba42","vcd":{"QN271AC":"register_pc","QN271RC":"d932156ad23bb851d5e72bd49d34ba42","QN271SL":"d932156ad23bb851d5e72bd49d34ba42"}}}
slideToken = response.json().get('data').get('cst')
print(slideToken)  #69c6a7642fc648ff0d51502ffdb99e88
# 发送验证码
sendLoginCode_url = 'https://user.qunar.com/weblogin/sendLoginCode'
data = {
    "usersource": "",
    "source": "",
    "ret": "https://www.qunar.com/",
    "ref": "",
    "business": "",
    "pid": "",
    "originChannel": "",
    "activityCode": "",
    "origin": "",
    "mobile": 15653613200,
    "prenum": 86,
    "loginSource": 1,
    "slideToken": slideToken,
    "smsType": 0,
    "appcode": "register_pc",
    "bella": "",
    "captchaType": ""
}

res = requests.post(sendLoginCode_url, data=data)
print(res.text)
