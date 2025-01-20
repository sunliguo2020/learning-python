# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-08-27 18:28
手动登录拼多多后，找到cookie，然后将cookie添加到代码中，实现自动登录拼多多。
实现功能
1、采集订单信息，导出到csv或excel文件中
"""
import csv
import os
import time
from io import BytesIO

import openpyxl
import requests
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def save2csv(orders):
    """
    将订单数据保存到csv文件中
    :param orders: 订单数据
    """
    # 保存到csv文件中
    with open('orders.csv', 'w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        # 写入表头
        writer.writerow(['商品名称', '商品图片', '商品属性', '商品数量', '商品价格', '实付金额'])
        # 写入数据
        writer.writerows(orders)


def save2xls(pdd_orders, save_file_name='orders.xlsx'):
    """
    将订单数据保存到Excel文件中
    """
    # 保存到Excel文件中
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['商品名称', '商品属性', '商品数量', '商品价格', '实付金额'])

    for order in pdd_orders:
        # 注意：Excel中不直接存储图片，但我们可以存储图片的路径
        # img_path = f"{os.path.basename(img_folder)}/{order[1].split('/')[-1]}"
        ws.append(order)

    wb.save(save_file_name)


def scroll_until_element_visible(driver, element_selector, timeout=600):
    """
    滚动页面直到找到指定的元素或超时。

    :param driver: Selenium WebDriver 实例
    :param element_selector: 一个元组，包含(By.XXX, 'selector')，用于定位元素
    :param timeout: 超时时间（秒）
    :return: 如果找到元素，则返回该元素；如果超时，则返回None
    """
    start_time = time.time()
    while True:
        try:
            # 尝试查找元素
            element = driver.find_element(*element_selector)
            # 如果元素可见（这里为了安全起见，可以加上EC.visibility_of_element_located，但这里直接返回）
            return element
        except NoSuchElementException:
            # 元素未找到，计算已过去的时间
            elapsed_time = time.time() - start_time
            # 如果超时，则抛出异常
            if elapsed_time > timeout:
                raise TimeoutException(f"Timed out after {timeout} seconds waiting for element to appear")
                # 否则，继续滚动页面
            # 这里使用JavaScript来滚动，因为Selenium没有直接滚动到页面底部的命令
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 等待一段时间以便页面加载新内容
            time.sleep(0.2)  # 根据页面加载速度调整这个值


def download_img(img_url, img_folder, img_name):
    """
    下载图片并保存到指定的文件夹。

    :param img_url: 图片的URL地址
    :param img_name:
    :param img_folder: 保存图片的文件夹路径
    :
    """
    # 确保文件夹存在
    os.makedirs(img_folder, exist_ok=True)
    # 下载图片
    response = requests.get(img_url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)

    # 检查并转换图像模式
    print(f"Original mode: {img.mode}")  # 打印原始模式

    # 检查图像模式，如果不是'RGB'或'L',则转换为'RGB'
    if img.mode not in ['RGB', 'L']:
        img = img.convert('RGB')
    # 构造图像文件名和路径
    img_filename = f"{img_folder}/{img_name}.jpg"

    # 保存图像之前再次打印模式以确保
    print(f"Final mode before saving: {img.mode}")
    # 保存图像
    img.save(img_filename)


def scroll_to_bottom(driver):
    """滚动浏览器页面到底部"""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# chrome 驱动
service = Service(r'd:/chromedriver-win64/chromedriver.exe')
browser = webdriver.Chrome(service=service)

# 我的订单页面
order_url = 'https://mobile.yangkeduo.com/orders.html'

browser.get(order_url)

# 操作cookie
# 1、获取cookie
cookies = browser.get_cookies()
# for cookie in cookies:
#     print(f"{cookie['name']}={cookie['value']}")

# 要添加的多个 cookie 需要先手动登录pdd，获取cookie

cookies = [
    {'name': 'JSESSIONID', 'value': '6A982A26D8ABF34AC9DB46828CE1C8AB', 'domain': 'mobile.yangkeduo.com',
     'path': '/'},
    {'name': 'PDDAccessToken', 'value': '5LPOIJ2KTPB54J5QNTU5ZV6TMUKU7ALB2FWBDD4WBFI4Y7QCC7AQ1209d00',
     'domain': 'mobile.yangkeduo.com', 'path': '/'}
]

# 遍历 cookies 列表并逐个添加
for cookie in cookies:
    browser.add_cookie(cookie)

# 再次访问
browser.get(order_url)

# 向下滚动
# <div class="loading-text">您已经没有更多的订单了</div>
#
for _ in range(200):
    time.sleep(0.5)  # 0.5s 防止被识别为 bot
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 调用函数滚动页面直到找到元素
# element_selector = (By.CLASS_NAME, 'loading-text')
# element = scroll_until_element_visible(browser, element_selector)
#
# if element.text == "您已经没有更多的订单了":
#     print("已到达页面底部，没有更多订单")

orders = []
order_list_div = browser.find_elements(By.XPATH, "//div[@class='_16zcITvZ']")

# 创建一个文件夹来保存图片
img_folder = 'order_images'
if not os.path.exists(img_folder):
    os.makedirs(img_folder)

for no, order_div in enumerate(order_list_div):
    product_name = order_div.find_element(By.XPATH, './/span[@data-test="商品名称"]').text
    if product_name:  # 确保找到了商品名称
        # 商品图片
        product_img_div = order_div.find_element(By.XPATH, './/div[@data-test="商品图片"]')
        product_img = product_img_div.find_element(By.TAG_NAME, 'img').get_attribute('src')
        product_img_url = product_img.split('?')[0]
        img_name = os.path.basename(product_img_url)
        # 下载图片
        download_img(product_img_url, img_folder, img_name)

        # 商品属性  //p[@class="_3CQR8Qs3"]
        product_attribute = order_div.find_element(By.CLASS_NAME, '_3CQR8Qs3').text

        # 商品价格
        product_price = order_div.find_element(By.XPATH, './/span[@data-test="商品价格"]').text

        # 商品数量
        product_quantity = order_div.find_element(By.CLASS_NAME, '_1X7_Iw3h').text

        # 实付金额
        total = order_div.find_element(By.CLASS_NAME, '_2hfIDJ43').text
        print(f"{no}:商品名称: {product_name},商品价格: {product_price},实付金额: {total}")

        """
        # 定位并点击进入详情页
        detail_em = order_div.find_element(By.XPATH, './/span[@data-test="商品名称"]')
        detail_em.click()
        time.sleep(2)  # 等一秒钟让详情页完全加载
        # 抓取其他信息
        scroll_to_bottom(browser)
        # 点击查看更多工单信息
        wait = WebDriverWait(browser, 10)  # 等待最多10秒
        order_more_info_em = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._1rH-5Y-Z")))
        # order_more_info_em = browser.find_element(By.CLASS_NAME, '_1rH-5Y-Z')
        order_more_info_em.click()

        # 使用XPath定位订单编号
        order_sn_xpath = "//span[contains(@class, '_31rGJ72q') and contains(@aria-label,'订单编号')]"
        order_sn_element = browser.find_element(By.XPATH, order_sn_xpath)
        order_sn = order_sn_element.text  # 提取订单编号文本

        # 使用XPath定位下单时间
        order_time_xpath = "//li[contains(@class, '_1OUQmHfz') and contains(@aria-label,'下单')]//span"
        order_time_element = browser.find_element(by=By.XPATH, value=order_time_xpath)
        order_time = order_time_element.text  # 提取下单时间文本
        print(f"订单号: {order_sn},下单时间: {order_time}")

        
"""
        orders.append((
            product_name,
            product_attribute,
            product_quantity,
            product_price,
            total))

        # 返回原窗口
        # 使用JavaScript回到上一页
        # browser.execute_script("window.history.go(-1)")

save2xls(orders, "pdd_orders-20241118.xls")

time.sleep(2000)
