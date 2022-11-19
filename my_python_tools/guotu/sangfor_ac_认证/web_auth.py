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

正常登录后的结果：
b"{'success':true, 'msg':'logon success','action':'logout','pop':0,'userName':'\xc3\xa6\xc2\x9e\xc2\x97\xc3\xa8\xc2\x90\xc2\x8d','location':'http://1.1.1.3/ac_portal/proxy.html?type=logout'}"
"""
import requests
import json


def web_auth(username='林萍', pwd='zrzy@2021'):
    """

    @param username:登录用户名
    @param pwd:登录密码
    @return:成功为1，失败为<0。
    """
    ac_url = 'http://1.1.1.3/ac_portal/login.php'
    post_data = {
        "opr": "pwdLogin",
        "userName": username,
        "pwd": pwd,
        "rememberPwd": "1"
    }

    try:
        req = requests.post(ac_url, data=post_data)
        result = req.text.encode('utf-8')
    except Exception as e:
        print("登录过程中错误,", e)
        return -1
    else:
        print("登录返回的结果为：", result)

    # 判断是否登录成功
    json_data = json.load(result)
    if json_data.get('sucess') is True \
            and json_data.get('msg') == 'logon success':
        return 1

if __name__ == '__main__':
    pass