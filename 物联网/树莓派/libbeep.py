# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-12 7:41
"""
import time

import RPi.GPIO as GPIO

PIN_NO = 12  # GPIO编号，可自定义

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NO, GPIO.OUT)


# 哔1次，时长作为参数传递
def beep(seconds):
    GPIO.output(PIN_NO, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(PIN_NO, GPIO.LOW)


# 哔N次，时长、间隔时长、重复次数作为参数传递
def beepAction(secs, sleepsecs, times):
    """

    @param secs:
    @param sleepsecs:
    @param times:
    @return:
    """
    for i in range(times):
        beep(secs)
        time.sleep(sleepsecs)


if __name__ == '__main__':
    beepAction(0.02, 0.02, 30)
