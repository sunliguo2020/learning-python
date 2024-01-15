# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-13 21:51
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://www.5xclass.cn/')

# 根据ID寻找
tag = driver.find_element(By.ID, "bs-example-navbar-collapse-1")
print(tag.text)
print(10 * "-")

# 根据类名寻找
tags = driver.find_elements(By.CLASS_NAME, "panel-heading")
for tag in tags:
    print(tag.text)
print(10 * "-")

# 根据标签名称寻找
tags = driver.find_elements(By.TAG_NAME, "li")
for tag in tags:
    print(tag.text)
print(10 * "-")

# 根据XPATH寻找
tag = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[1]")
print(tag.text)
print(10 * "-")

# 根据XPATH寻找
tag = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[1]/a')
print(tag.text)
print(10 * "-")

# 根据XPATH寻找多个
tags = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a')
for tag in tags:
    print(tag.text)
print(10 * "-")

# 根据父子关系嵌套寻找
parent = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div')
tags = parent.find_elements(By.XPATH, "div[@class='course']/a")
for tag in tags:
    print(tag.text)

time.sleep(5)
driver.close()