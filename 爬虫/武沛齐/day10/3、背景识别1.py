# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/23 19:07
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 1、图片.py
 @Project : learning-python
"""
import time
from io import BytesIO

import ddddocr
from PIL import Image
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

# 5、识别任务图片
ocr = ddddocr.DdddOcr(show_ad=False)
word = ocr.classification(geetest_ques_tips_tag.screenshot_as_png)
print(f'要识别的文字：{word}')

# 6、背景geetest_bg
geetest_bg_tag = driver.find_element(By.CLASS_NAME, 'geetest_bg')
geetest_bg_tag.screenshot('geetest_bg.png')

content = geetest_bg_tag.screenshot_as_png

# 7、识别背景中的所有文字并获取坐标
ocr = ddddocr.DdddOcr(show_ad=False, det=True)
poses = ocr.detection(content)

print(f"poses:{poses}")

# 8、循环坐标中的每个文字并识别
bg_word_dict = {

}

img = Image.open(BytesIO(content))

for box in poses:
    x1, y1, x2, y2 = box
    # 根据坐标获取每个文字的图片
    corp = img.crop(box)
    img_byte = BytesIO()
    corp.save(img_byte, 'png')

    # 识别文字
    ocr2 = ddddocr.DdddOcr(show_ad=False)
    word = ocr2.classification(img_byte.getvalue())

    # 获取每个字的坐标
    bg_word_dict[word] = [int((x1+x2)/2),int((y1+y2)/2)]

print(bg_word_dict)

time.sleep(200)

driver.close()
