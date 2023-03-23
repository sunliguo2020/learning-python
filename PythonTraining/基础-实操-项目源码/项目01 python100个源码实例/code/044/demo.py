import string
f = open('./data/split.txt')
s=f.read()
str1=s.title()
print(str1)
print("".join([s for s in str1.splitlines(True) if s.strip()]))
list1 = str1.split() # 采用默认分隔符进行分割
#字符串列表去重
l1=list(set(list1))
l1.sort(key=list1.index)
for i in l1:
  #去掉特殊符号
  i1=i.translate(str.maketrans('', '', string.punctuation))
  i2=i1.strip(' \t\n\r')# 去除字符串中头尾的空格
  #print(i1.strip(' \t\n\r')) # 去除字符串中头尾的空格
  if not i2.isnumeric():   #滤除数字
        i3=i2
        f1 = open('./data/split副本.txt','a')
        f1.write('\n'+i3)
