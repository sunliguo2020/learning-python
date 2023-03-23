
import winsound
import win32com
from win32com.client import Dispatch, constants
import random
import time
speak_out = win32com.client.Dispatch('sapi.spvoice')
lang={}


def view():                                    # 按字典顺序输出方言
    for key,value in lang.items():
        print(key,":",value)                   # 按字典顺序显示方言   
        speak(key+"     "+value)               # 按字典顺序语音播放方言
        time.sleep(1)                          # 循环间隔时间为1秒钟
def speak(str):                                # 按播放语音
    speak_out.speak(str)                       # 输出方言解释
    winsound.PlaySound(str,winsound.SND_ASYNC)   # 输出结束音
with open("note.txt","r",encoding='UTF-8') as file: # 读取文件中的方言给字典
    while True:
       line = file.readline()
       if line =='':            
           break
       group=line.split("：")           # 按“：”分割字符串
       lang[group[0]]=group[1] 
print("    东北方言\n")
print("说明：输入“q”退出系统；输入“s”按顺序输出并朗读词典内容。")
while True:
    word=input("请输入要查找的东北方言：").strip()
    if word.lower()=="q":
        break
    if word.lower()=="s":
        view()
    else:
        note=lang.get(word,"no")
        if note!="no":
            print(word,":",note)
            speak(word+":    "+note)
        else:
            print("没有检索到相关东北方言！")
