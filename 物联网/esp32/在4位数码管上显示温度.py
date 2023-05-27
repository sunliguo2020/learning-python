# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-27 13:41

通过dht11 模块获取当前的温度和湿度，在4位数码管显示。
物理连接：
4位数码管：  ESP32 IO
CLK --->    16
DIO --->    18
VCC --->    5V
GND --->    GND
DHT11 :
VCC --->    5V
DAT --->    17
GND --->    GND
"""
import time

import dht
import tm1637
from machine import Pin

dht11_pin = 17
clk_pin = 16
dio_pin = 18


# 获取当前温度和湿度的函数
def get_temp_humi():
    # 定义DHT11控制对象
    dht11 = dht.DHT11(Pin(dht11_pin))
    time.sleep(0.5)
    dht11.measure()  # 调用DHT类库中测量数据的函数
    temp = dht11.temperature()
    humi = dht11.humidity()

    if temp is not None and humi is not None:
        return temp, humi
    else:
        return None


def show_temp_humi():
    # 定义数码管控制对象
    smg = tm1637.TM1637(clk=Pin(clk_pin), dio=Pin(dio_pin))
    temp, humi = get_temp_humi()

    smg.scroll(str(temp) + "-" + str(humi), 500)


if __name__ == '__main__':

    while True:
        time.sleep(1)
        show_temp_humi()