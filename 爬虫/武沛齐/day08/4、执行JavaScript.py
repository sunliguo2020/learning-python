# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-13 23:27
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

# #############  1.点击短信登录 #############
time.sleep(3)
sms_btn = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()


# #############  2.输入账号 #############
phone_txt = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input'
)
phone_txt.send_keys("18630087660")

# ############# 3.选择国家 #############
time.sleep(2)
driver.execute_script('document.querySelector(".area-code-select").children[18].click()')

# ############# 4.读取cookie #############
data_string = driver.execute_script('return document.cookie;')   # return document.title;
print(data_string)

# ############# 5.读取cookie #############
cookie_list = driver.get_cookies()
print(cookie_list)

time.sleep(2550)
driver.close()