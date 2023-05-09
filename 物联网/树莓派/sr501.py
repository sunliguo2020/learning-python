# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-09 12:54
"""
import time

import RPi.GPIO as GPIO

"""
import json
import paho.mqtt.client as mqtt


# 发布客户端

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('1.116.67.152', 1883, 60)  # 60为keepalive的时间间隔
client.subscribe('Sub/100026', qos=0)
client.loop_start()  # 保持连接
"""


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)


def beep():
    for i in range(1, 6):
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)
        print("the Buzzer will make sound")


def ledon():
    for i in range(1, 10):
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(18, GPIO.HIGH)


def detct():
    for i in range(1, 31):
        if GPIO.input(17):
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Someone is closing!")
            c = {"man": 1}
            ledon()
            """
            client.publish('Pub/100026', payload=json.dumps(c), qos=0)  # 上传数据
            beep()
            """
        else:
            GPIO.output(18, GPIO.LOW)  # 无人时关闭蜂鸣器
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Noanybody!")

            """
            c = {"man": 0}
            client.publish('Pub/100026', payload=json.dumps(c), qos=0)  # 上传数据
            """
        time.sleep(3)  # 每3秒检查一次


time.sleep(2)
init()
detct()
GPIO.cleanup()
