info=['零','一','二','三','四','五','六','七','八','九']
data=input("请输入数字:")
for i in range(len(data)):
     print(info[int(data[i])],end='')
