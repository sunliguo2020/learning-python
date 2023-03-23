# *_* coding : UTF-8 *_*

# 文件名称   ：demo04.py
# 开发工具   ：PyCharm
gem=[["大众",643518],["奔驰",319163],["宝马",265051],["福特",252323],["雪铁龙",227967],["奥迪",255300]]
fra=[["雪铁龙", 698985],["雷诺",547704],["大众",259268],["福特",82633],["宝马",84931],["奔驰",73254]]
eng=[["福特",254082],["大众",203150],["雪铁龙",177298],["奔驰",172238],["宝马",172048],["奥迪",143739]]
for item1,item2,item3 in zip(gem,fra,eng):
    print(item1[0],item1[1],"  ",item2[0],item2[1],"  ",item3[0],item3[1])

for item1,item2,item3 in zip(gem,fra,eng):
    item11 = item1[0].ljust(8)
    item12 = str(item1[1]).ljust(8)
    item21 = item2[0].ljust(8)
    item22 = str(item2[1]).ljust(8)
    item31 = item1[0].ljust(8)
    item32 = str(item3[1]).ljust(8)
    print(item11 +"\t",item12+"\t","  ",item21+"\t",item22+"\t","  ",item31+"\t",item32)

