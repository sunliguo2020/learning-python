# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-09 19:21
控制led闪烁
"""

import time

#
import RPi.GPIO as GPIO

led = 18  # 这里使用的是18引脚，请根据自己使用的引脚编号修改
# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
n = 0  # 用于控制闪烁次数
while n < 30:
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.05)
    n += 1
