# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：recaudio.PY
# 开发工具   ：PyCharm
'''
  识别mp3语音时如何转换为采用16K采样率的wav文件
'''
from aip import AipSpeech
import os
import uuid
import time

APP_ID = '自己的百度云应用APPID'  # 设置自己创建百度云应用时的ID
API_KEY = '自己的百度云应用APIKey'  # 设置自己创建百度云应用时的APIKey
SECRET_KEY = '自己的百度云应用SECRETKey'  # 设置自己创建百度云应用时的SECRETKey

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY) # 创建语音识别对象
filepath=input('请输入要识别的音频文件：') # 记录用户输入的音频文件地址

# # 直接识别，会出现3301错误，表示音频采样率不符合，或者音质不清晰
# with open(filepath, 'rb') as f: # 以二进制形式打开文件
#     # 识别音频文件内容
#     result=client.asr(f.read(), 'wav', 16000, {'dev_pid': 1536,})
#     print(result) # 输出识别结果

path=os.path.splitdrive(filepath)[0] # 得到原视频的路径
if not path.endswith('\\'): # 判断路径是否以\结尾
    path=path+'\\' # 为路径结尾增加\
newaudio = uuid.uuid1() # 随机生成临时文件名
newfile=os.path.join(path,str(newaudio) + ".wav") # 新的文件（包含路径和扩展名）
# 定义使用ffmpeg转换视频的命令，将mp3格式转换为采用16K采样率的wav文件
cmd = "ffmpeg -i " + str(filepath) + " -ar 16000 -ac 1  -f wav " + newfile
os.popen(cmd) # 执行格式转换命令
time.sleep(0.1) # 休眠0.1秒，这里主要是为了执行上面的转换操作
if os.path.exists(newfile): # 判断是否存在新转换的文件
    with open(newfile, 'rb') as f: # 以二进制形式打开文件
        # 识别音频文件内容
        result=client.asr(f.read(), 'wav', 16000, {'dev_pid': 1536,})
        print(result['result']) # 输出识别结果
else:
    print('没有该文件')


