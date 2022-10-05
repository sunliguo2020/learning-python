# -*- coding: utf-8 -*-
"""
 @Time : 2022/10/5 17:48
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : confirmed_users.py
 @Project : github
"""
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())