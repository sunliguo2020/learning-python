# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/19 19:11
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 注册滑块.py
 @Project : learning-python
"""
import time

# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# 打开chrome浏览器
service = Service('../288job/chromedriver-win64/chromedriver.exe')
d = webdriver.Chrome(service=service)
d.maximize_window()
d.implicitly_wait(10)
# 打开携程网注册页面
d.get('https://passport.ctrip.com/user/reg/home')
# 点击同意并继续
d.find_element(By.XPATH, '//div[@class="pop_footer"]/a[@class="reg_btn reg_agree"]').click()
# 定位到滑块按钮元素
ele_button = d.find_element(By.XPATH, '//div[@class="cpt-drop-btn"]')
# 打印滑块按钮的宽和高
# print('滑块按钮的宽：', ele_button.size['width'])
# print('滑块按钮的高：', ele_button.size['height'])
# 定位到滑块区域元素
ele = d.find_element(By.XPATH, '//div[@class="cpt-bg-bar"]')
# 打印滑块区域的宽和高
# print('滑块区域的宽：', ele.size['width'])
# print('滑块区域的高：', ele.size['height'])
# 拖动滑块
ActionChains(d).drag_and_drop_by_offset(ele_button, ele.size['width'], ele.size['height']).perform()


time.sleep(50)