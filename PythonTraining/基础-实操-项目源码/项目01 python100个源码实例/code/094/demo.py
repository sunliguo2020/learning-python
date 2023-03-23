type_num="BRM8S"
date="2021:12:28"
date=date.split(":")
year_num=date[0][2:]
month=hex(int(date[1])).replace("0x","")
day=date[2] 
date_num=year_num+month+day
start=100
count=int(input("请输入要生成的产品序列号（SN）数量："))
sn=""
for i in range(count):
    num=type_num+date_num+str(start+i).zfill(5)
    sn+=num+"\n"
print(sn)
