# -*- coding: utf-8 -*-
"""
 @Time : 2022/10/5 17:44
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : cities.py
 @Project : github
"""
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city  = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")