import requests
from requests.exceptions import RequestException
import tkinter as tk
#定义翻译函数
def translate():
        str1 = text1.get()  # 定义一个变量，用来接收输入文本框的值
        data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': str1  # 将输入文本框中的值赋值给接口参数
        }
        url = "http://fanyi.youdao.com/translate"
        try:
            r = requests.get(url, params=data)
            if r.status_code == 200:
                result = r.json()
                translate_result = result['translateResult'][0][0]["tgt"]
                text2.delete(1.0, "end")  # 清空输出文本框
                text2.insert('end',translate_result)  # 将翻译结果添加到输出文本框中
        except RequestException:
            text2.insert('end', "发生错误")
#定义写入文本txt的函数
def write():
  f1 = open('./data/translate.txt','a+')
  f1.write(text1.get()+','+text2.get(0.0,tk.END))
#定义清空文本框的函数
def delete():
  text1.delete(0,"end") # 从第一行清除到最后一行
  text2.delete(1.0,"end")  


window = tk.Tk()  #创建window窗口
window.title("明日mini翻译器")  # 定义窗口名称
text1 = tk.Entry(window, width=80,bg='whitesmoke')  # 在窗体上添加一个输入文本框,并设置尺寸和颜色
text2 = tk.Text(window, height=18,bg='lightgrey')   # 在窗体上添加一个输出文本框，并设置尺寸和颜色
text1.grid(row=0,sticky="W",padx=1)
text2.grid(row=1)

# 添加一个按钮，用于触发翻译功能
t_button = tk.Button(window, text='翻译', relief=tk.RAISED, width=8, height=1,font='宋体',bg='red',fg='white',command=translate)
# 添加一个按钮，用于触发清空输入文本框
button1 = tk.Button(window, text='保存',font='宋体', relief=tk.RAISED, width=8, height=1, command=write)
# 添加一个按钮，用于触发清空输出文本框
button2 = tk.Button(window, text='清空',font='宋体', relief=tk.RAISED,width=8, height=1, command=delete)
# 添加背景图片
image_file = tk.PhotoImage(file='mr.png')
label= tk.Label(window, image=image_file)
#完成界面布局，设置各个控件的位置
t_button.grid(row=0,column=1,padx=2)
button1.grid(row=0, column=2, padx=2)
button2.grid(row=0,column=3,padx=2)
label.grid(row=1, column=1,columnspan=3)
tk.mainloop()


