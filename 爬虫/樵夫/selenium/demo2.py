# -*- coding: utf-8 -*-
"""
 @Time : 2024/8/25 21:58
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from selenium import webdriver

web = webdriver.Chrome(executable_path='./chromedriver.exe')

url = 'https://www.lagou.com/wn/'

web.get(url)
print(web.title)