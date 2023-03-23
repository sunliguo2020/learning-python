import difflib
import tkinter as tk
import tkinter.filedialog
#打开文件
def button1():
  global file1
  file1=tk.filedialog.askopenfilename()
  txt_path1.set(file1)
#打开文件
def button2():
  global file2
  file2=tk.filedialog.askopenfilename()
  txt_path2.set(file2)
#对比文件
def Diff():
  with open(file1) as f1,open(file2) as f2:
    text1 = f1.readlines()
    text2 = f2.readlines()
  d = difflib.HtmlDiff()
  with open('result1.html','w') as f:
    f.write(d.make_file(text1,text2))

#建立主窗口window
window = tk.Tk()
#设置窗口标题栏名称
window.title('用Python实现文件对比分析')
#设置窗口的大小
window.geometry('650x200')
# 在主窗口添加标签
label = tk.Label(window, text='请选择需要对比的文 件：',fg='blue',font=('Arial', 12)).place(x=30, y=30)
l1 = tk.Label(window, text='原 文 件：', font=('Arial', 12)).place(x=30, y=80)
l2=tk.Label(window, text='目标文件：', font=('Arial', 12)).place(x=30, y=110)
# 在主窗口添加文本框
txt_path1 = tk.StringVar()
text1 = tk.Entry(window,textvariable=txt_path1, show = None,width=60)
txt_path2= tk.StringVar()
text2 = tk.Entry(window,textvariable=txt_path2,show = None,width=60)
text1.place(x=120,y=80)
text2.place(x=120,y=110)
# 在主窗口添加命令按钮
button1 = tk.Button(window,width=8, height=1,text='选择文件',bg='skyblue',command=button1).place(x=550, y=80)
button2 = tk.Button(window,width=8, height=1,text='选择文件',bg='skyblue',command=button2).place(x=550, y=110)
button3 = tk.Button(window,width=20, height=1,text='文件对比',fg='red',bg='orange',command=Diff).place(x=220, y=150)
# 主窗口循环显示
window.mainloop()
