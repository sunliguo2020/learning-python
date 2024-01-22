# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/18 22:36
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 滑动登录.py
 @Project : learning-python
"""
import io
import re
import time

from PIL import Image
import ddddocr
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service = Service('./chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.288job.cn/')

# 关闭广告
# <span id="yhq_tip_close" class="tcbanner_gb">关闭</span>
tag = driver.find_element(By.ID, "yhq_tip_close")
# print(tag.text)
# 关闭广告
print('关闭广告')
tag.click()

# 准备登录
# 手机登录 <li id="ajaxmobile_login" class="login_box_h_list_cur">手机登录<i></i></li>
mobile_login_tag = driver.find_element(By.ID, 'ajaxmobile_login')
mobile_login_tag.click()

# 输入手机号
mobile_input_tag = driver.find_element(By.ID, 'ajaxusermoblie')
mobile_input_tag.send_keys('15244426664')

# 发送验证码 ajaxsend_msg_tip
send_msg_tag = driver.find_element(By.ID, 'ajaxsend_msg_tip')
send_msg_tag.click()

time.sleep(2)


# 获取背景图片
def fetch_bg_func(dv):
    driver.switch_to.frame('tcaptcha_iframe_dy')
    tag_obj = dv.find_element(
        By.ID, 'slideBg'
    )
    style_string = tag_obj.get_attribute('style')
    # 获取背景图片大小
    match_list = re.findall('url\(\"(.*)\"\);', style_string)
    if match_list:
        return match_list[0]


bg_image_url = WebDriverWait(driver, 30, 0.5).until(fetch_bg_func)
print('背景图', bg_image_url)


# 获取缺口图片

def fetch_slice_func(dv):
    tag_obj = driver.find_element(
        By.XPATH,
        '//*[@id="tcOperation"]/div[8]'
    )
    print('缺口图截图')
    tag_obj.screenshot('slice_screenshot.png')
    style_string = tag_obj.get_attribute('style')
    match_list = re.findall('url\(\"(.*)\"\);', style_string)
    if match_list:
        return match_list[0]


slice_image_url = WebDriverWait(driver, 30, 0.5).until(fetch_slice_func)

print("缺口图", slice_image_url)

# 识别图片

# 获取图片
slice_bytes = requests.get(slice_image_url).content
bg_bytes = requests.get(bg_image_url).content

# 调整背景图片大小
# 背景图原始尺寸：672：390
image = Image.open(io.BytesIO(bg_bytes))
# 调整图像大小为宽度为340 像素，高度为243像素
resized_image = image.resize((340, 243))

bg_bytes = io.BytesIO()
resized_image.save(bg_bytes, 'png')
# bg_bytes = bg_bytes.read()
resized_image.save('bg.png')

# 保存原始缺口图片
with open('slice.png', 'wb') as fp:
    fp.write(slice_bytes)

# with open('bg.png', 'wb') as fp:
#     fp.write(bg_bytes)

# 裁剪得到缺口图
img = Image.open('slice.png')
print(img.size)

# 裁剪图片需要优化
cropped = img.crop((150, 490, 240, 588))  # (left, upper, right, lower)
# 缩放图片
cropped = cropped.resize((60, 60))
cropped.save("slice2.png")

with open('slice2.png', 'rb') as fp:
    slice_bytes = fp.read()

with open('bg.png', 'rb') as fp:
    bg_bytes = fp.read()

# 使用ddddocr识别
slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
res = slide.slide_match(slice_bytes, bg_bytes, simple_target=True)

x1, y1, x2, y2 = res['target']

print('滑动距离', x1)

# 滑动按钮
# driver.switch_to.default_content()
btn_tag = driver.find_element(By.XPATH, '//*[@id="tcOperation"]/div[6]')
# print(btn_tag)

ActionChains(driver).click_and_hold(btn_tag).perform()
ActionChains(driver).move_by_offset(xoffset=x1, yoffset=0).perform()
ActionChains(driver).release().perform()

print('移动完成')

time.sleep(500)
