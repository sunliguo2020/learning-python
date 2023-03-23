usergroup=[]
menu=["B超室","化验室"]
i=1
file = open('patient.txt')         # 以只写模式打开文件
while True:
    line= file.readline().strip(' ').strip('\n')     # 读取患者信息
    if line== '':              # 如果信息为空
        break                   # 跳出循环
    user=line.split(",")
    usergroup=usergroup+user
file.close()              # 关闭文件
user1=usergroup[0::2]
user2=usergroup[1::2]
print("="*35)
print("电子科分组排队系统 ".center(25))
print("="*35)
print((menu[0] +"             "+ menu[1]).center(25))
template="{}"
for item1,item2 in zip(user1,user2):
    len1=len(item1.encode("gbk"))
    len0=len(item1)
    len3=round((len1-len0)/2)-1
    item3="A%03d"% i +" "+ item1
    item4="B%03d"% i +" "+ item2
    print (item3.ljust(18-len3 ) +  item4  )
    i=i+1
