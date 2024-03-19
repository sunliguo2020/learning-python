# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/18 20:31
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('./chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 打开网页
# driver.get('https://passport.bilibili.com/login')
driver.get('https://www.sgjhw.com/web/login?redirect=%2Fregister')

# 输入手机号
# phone_tag = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/form/div[1]/div/div[1]/input')
phone_tag = driver.find_element(By.XPATH, '')
print(phone_tag)
for tag in phone_tag:
    print(tag.text)

# phone_tag.send_keys('<PASSWORD>')
#


time.sleep(100)
driver.close()
