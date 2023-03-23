import tkinter as tk
from PIL import Image,ImageTk 
import sys
import tkinter.filedialog

#先将图片填充为正方形
def fill_image(image): 
 width, height = image.size 
 #比较图片的宽和高，选取值较大的作为新图的宽 
 newImage_width = width if width > height else height 
 #生成正方形图，空白处用白色填充
 newImage = Image.new(image.mode, (newImage_width, newImage_width), color='white')  
 #如果原图宽大于高，则填充图片的竖直维度
 if width > height: 
    newImage.paste(image, (0, int((newImage_width - height) / 2))) 
 else: 
    newImage.paste(image, (int((newImage_width - width) / 2),0)) 
 return newImage 
# 切图（切成9张图）
def cut_image(image):
 width, height = image.size
 colWidth = int(width / 3)   #一行3张
 image_grid = []
 for i in range(0,3):
   for j in range(0,3):
      row = (j*colWidth,i*colWidth,(j+1)*colWidth,(i+1)*colWidth)
      image_grid.append(row)
 image_list = [image.crop(row) for row in image_grid]
 return image_list

#保存图片
def save_images(image_list): 
 index = 1
 for image in image_list: 
   image.save(str(index) + '.png', 'PNG') 
   index+=1
# 单击选择图片按钮，选择并显示图片
def select_button():
  global a
  a=tk.filedialog.askopenfilename()
  #显示图片
  img = Image.open(a)
  out = img.resize((310,280))   #设置图片的大小
  #out.save("new.png") #保存图片
  render = ImageTk.PhotoImage(out)
  img = tkinter.Label(image=render)
  img.image = render
  img.place(x=30, y=60)
  txt.set(a)  #显示图片文件路径
  
# 单击切分图片按钮，实现图片分割
def cut_button():
  file_path=a # 获取图片路径
  image = Image.open(file_path) 
  image_new = fill_image(image) 
  image_list = cut_image(image_new)
  save_images(image_list) 
  label1.config(text='切图成功!请在程序所在目录查看！')
# 设置窗口
main=tk.Tk()
#设置窗口的大小
main.geometry('400x400')
main.title('明日九宫格切图器')       #设置标题栏
main.iconbitmap('mr.ico')   #窗口图标
label1=tk.Label(main,text='显示要切分图片的文件路径：',fg='blue')
label1.pack()
txt = tkinter.StringVar()
txt_entry = tkinter.Entry(main, width=55, textvariable=txt)
txt_entry.pack()
button1=tk.Button(main,width=10, height=1,text='选择图片',fg='red',bg='yellow',command=select_button).place(x=30, y=360)
button2=tk.Button(main,width=10, height=1,text='切分图片',fg='red',bg='green',command=cut_button).place(x=120, y=360)
main.mainloop() # 执行主循环

