# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-08-02 10:28
POST /ac_portal/login.php HTTP/1.1
Host: 1.1.1.3
Connection: keep-alive
Content-Length: 70
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://1.1.1.3
Referer: http://1.1.1.3/ac_portal/default/pc.html?tabs=pwd
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Sessionid=3243203828-1; ac_login_info=passwork

opr=pwdLogin&userName=%E6%9E%97%E8%90%8D&pwd=zrzy%402021&rememberPwd=1
"""
import requests

ac_url = 'http://1.1.1.3/ac_portal/login.php'
post_data = {
    "opr": "pwdLogin",
    "userName": "林萍",
    "pwd": "zrzy@2021",
    "rememberPwd": "1"
}
req = requests.post(ac_url,data=post_data)
print(req.text.encode('utf-8'))