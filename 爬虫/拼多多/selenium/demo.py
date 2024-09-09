# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-08-24 18:09
接受手机验证码自动登录拼多多
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'd:/chromedriver-win64/chromedriver.exe')
# 打开浏览器时的相关配置，可以根据需求进行打开和关闭
options = Options()
options.add_argument("--start-maximized")  # 启动时最大化窗口
# options.add_argument("--disable-blink-features=AutomationControlled")  # 使浏览器不显示自动化控制的信息
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
# driver.get('https://passport.bilibili.com/login')
pdd_url = 'https://mobile.yangkeduo.com/orders.html?type=0&comment_tab=1&combine_orders=1&main_orders=1&refer_page_name=personal&refer_page_id=10001_1724409662228_a14cydbnsw&refer_page_sn=10001'
driver.get(pdd_url)
# 手机登录
phone_button = driver.find_element(By.CLASS_NAME, 'phone-login')
phone_button.click()
# 输入手机号
phone_input = driver.find_element(By.ID, 'user-mobile')
phone_input.send_keys('15689266171')
#  获取验证码
code_button = driver.find_element(By.ID, 'code-button')
code_button.click()

# 输入验证码
code_input = driver.find_element(By.ID, 'input-code')
code_msg = input('请输入验证码:')
code_input.send_keys(code_msg)

# 同意
agree_button = driver.find_element(By.CLASS_NAME, 'agreement-icon')
agree_button.click()

# 登录
login_button = driver.find_element(By.ID, 'submit-button')
login_button.click()

react_base_list = driver.find_element(By.XPATH, '//*[@id="base-list0"]/div[1]')
item_list = driver.find_elements(By.CLASS_NAME, '_16zcITvZ')
for item in react_base_list:
    pass

time.sleep(1000)

driver.close()
