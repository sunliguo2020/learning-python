# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-11-18 21:40
本程序用于国土局政务网小主机开机后网络认证和ssh反向代理
1、网络认证
2、
    autossh -M 4444 -NR 3333:localhost:22  sunliguo@aliyun.sunliguo.com -f -p 22334
"""
import os
import socket


def isNetOk(testserver='www.baidu.com', port=443):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex((testserver, port))
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False

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
    if not isNetOk():
        web_auth()
    else:
        try:
            os.system('autossh -M 4444 -NR 3333:localhost:22  sunliguo@aliyun.sunliguo.com -f -p 22334')
        except Exception as e:
            print("反向代理过程中出错:",e)