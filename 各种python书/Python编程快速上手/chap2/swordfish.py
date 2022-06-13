# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/28 21:04
"""
while True:
    print('Who are you?')
    name = input()
    if name != "Joe":
        continue
    print("Hello Joe.What is the password?(It is a fish)")
    password = input()
    if password == 'swordfish':
        break
print('Access granted')