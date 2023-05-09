# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-09 13:07
"""

# 目前用的人体红外传感器模块是最迷你型的，因此感应的距离只有一米
# 当检测到人体活动时，会持续高电平2～4秒

import time

import RPi.GPIO as GPIO

HC_SR501 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(HC_SR501, GPIO.IN)

try:
    while True:
        if GPIO.input(HC_SR501):
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 警告!附近一米内有人 ")
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 无情况，周围没人! ")
        time.sleep(1)

except:
    pass

GPIO.cleanup()
