# -*- coding: utf-8 -*-
"""
 @Time : 2022/10/5 9:24
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : parrot.py
 @Project : github
"""
prompt  = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
# message = input("Tell me something,and I will repeat it back to you:")
# print(message)
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)