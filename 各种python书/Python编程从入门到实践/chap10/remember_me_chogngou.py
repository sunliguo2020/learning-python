# -*- coding: utf-8 -*-
"""
 @Time : 2022/6/15 20:15
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : remember_me_chogngou.py
 @Project : github
"""
import json


def greet_user():
    """
    问候用户，并指出其名字
    """
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input('what is your name?')
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back,{username}")
    else:
        print(f"Welcome back,{username}")


greet_user()
