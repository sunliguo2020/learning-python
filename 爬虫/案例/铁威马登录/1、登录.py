# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/22 20:38
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 1、登录.py
 @Project : learning-python
"""
import requests

login_url = 'http://192.168.1.207:8181/tos/index.php?user/loginSubmit'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",

}
# 1、登录一次获取cookie

resp1 = requests.get(login_url)
cookie_dict = resp1.cookies.get_dict()

# 2 、第二次获取cookie中的token
token_url = 'http://192.168.1.207:8181/tos/index.php?share/common_js'
cookie_dict.update(requests.get(token_url).cookies.get_dict())
print(cookie_dict)

data = {
    'name': 'admin',
    'check_code': 'undefined',
    'password': 'c3VuI2dhb0BHRTIwMjI=',
    'rember_password': '0',
}

"""
    core.httpPost("./index.php?user/loginSubmit", {
                name: urlEncode(e),
                check_code: $("input.check_code").val(),
                password: base64_encode(t),
                rember_password: a
            })
"""
token = cookie_dict.get('tos_token')

headers.update({'Token': token,
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'http://192.168.1.207:8181/tos/index.php?user/login',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', })

print(headers)
resp = requests.post(login_url,
                     data=data,
                     headers=headers,
                     cookies=cookie_dict)
print(resp.json())
