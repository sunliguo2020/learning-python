# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/23 19:07
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 1、图片.py
 @Project : learning-python
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service = Service('../day08/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 1、打开首页
driver.get('https://www.geetest.com/adaptive-captcha-demo')

# 2、文字点选验证
wenzi_tag = driver.find_element(By.XPATH,
                                '//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[1]/div[2]/div[3]/div[4]')
wenzi_tag.click()

# 3、点击按钮开始验证
yanzheng_tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.CLASS_NAME, 'geetest_btn_click'))

print(yanzheng_tag.text)
yanzheng_tag.click()
time.sleep(2)
# 4、开始截图
geetest_ques_tips_tag = driver.find_element(By.XPATH,
                                            '//*[@id="captcha"]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]')
geetest_ques_tips_tag.screenshot('geetest_ques_tips.png')

# 5、背景geetest_bg
geetest_bg_tag = driver.find_element(By.CLASS_NAME, 'geetest_bg')
geetest_bg_tag.screenshot('geetest_bg.png')
time.sleep(200)
