import tkinter.filedialog
from tkinter import *
root = Tk()                                         # 建立根窗口
root.withdraw()                                     # 不显示窗口
filename =tkinter.filedialog.askopenfilename()      # 选择小说文件
with open(filename,'r') as file:                   # 打开小说文件
    list= file.readlines()                     # 读取全部文字到列表
word='\n'.join(list)                                # 分解成字符串
print(word )
new=word                                   # 创建统计字符串文字字符串
punct='， 。 ‘ ； ： （ ） ’ “ ” \n'      # 要去除的标点符号，间隔为中文空格
list_punct=punct.split(' ')
for item in list_punct:
    new.replace(item,'')                         # 删除小说中的标点符号
long=len(new)                                  # 获取纯文本的字数
user=input('输入统计词，如果多词用英文逗号间隔:\n').split(",")
for item in  user:                                 # 对每个词进行统计
   count=word.count(item)                          # 统计出现次数
   order=''                                        # 记录词出现位置
   size=0                                          # 临时记录词的位置
   for i in range(count):                          # 统计词出现的位置
       size=word.find(item,size+len(item)) 
       order+=str(size)+"  "                       # 累计出现的位置
   print("小说字数（去除标点）：",len(new))
   print(item+"出现次数：",count)
   print(item+"出现位置："+order)
   print(item+"出现频次：",format(count * len(item)/long,'.2f'))  
