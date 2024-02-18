# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/16 23:33
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import execjs


def password_encrypt(pwd, username):
    with open('pc_login_new.js', 'r', encoding='utf-8') as f:
        js_obj = execjs.compile(f.read())
    enc_res = js_obj.call("getUnPwd", pwd, username)
    print(f"加密后的用户名：{enc_res[0]}")
    print(f"加密后的密码：{enc_res[1]}")


if __name__ == '__main__':
    password_encrypt('15232', 'sunliguo')
