# _*_ coding:utf-8   _*_
# 文件名称：main.py
# 开发工具：PyCharm
import win32api
import win32con
from PIL import Image,ImageTk
import tkinter

import base64
import os
from tmp import img as tmpimg
app = tkinter.Tk()
app.title("打包图片")
app.resizable(False,False)
app['width'] = 220
app['height'] = 220
label =tkinter.Label(app,text="淡泊宁静",justify=tkinter.RIGHT,width= 100)
label.place(x=50,y=5,width=100,height=50)
#使用时需要解码
tmp = open('tmp.jpg', 'wb+')    #临时文件，用来保存JPG文件
tmp.write(base64.b64decode(tmpimg))
tmp.close()   # 关闭文件

image = Image.open('./tmp.jpg')  # 打开文件
img = ImageTk.PhotoImage(image)  # 使用PIL模块读取图片
l1 = tkinter.Label(app)  # 创建Label对象
l1.config(image=img)  # 指定要显示的图片
l1.place(x=10,y=50,width=200,height=160)  # 指定Label的显示位置
app.mainloop()    # 显示窗体
image.close()
os.remove('tmp.jpg')  # 删除文件
