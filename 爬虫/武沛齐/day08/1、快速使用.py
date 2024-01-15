# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-13 19:34
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
谷歌驱动的下载：
114及之前版本： http://chromedriver.storage.googleapis.com/index.html
117/118/119版本： https://googlechromelabs.github.io/chrome-for-testing/
"""
service = Service('./chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# driver.get('https://passport.bilibili.com/login')
driver.get('http://www.sunliguo.com')

time.sleep(5)


driver.quit()
