# -*- coding: utf-8 -*-
"""
 @Time : 2024/8/25 20:58
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 基于selenium 4.X
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = 'https://www.lagou.com/wn/'

service = Service(r'F:\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(url)
print(driver.title)
