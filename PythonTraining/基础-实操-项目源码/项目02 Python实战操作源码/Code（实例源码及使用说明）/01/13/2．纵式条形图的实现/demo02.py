# *_* coding : UTF-8 *_*
# 文件名称   ：demo02.py
# 开发工具   ：PyCharm
# 添加数据标签，显示市值
chart=[['alibaba',4580],['amazon',9628],['apple',11331],['oracle',2053]]
hchartall=900           # 条形图数据单位长度
mark=chr(0x25a0)        # 填充条形图的字符为方块
datazip=[]              # 量化后的比较数据
horiz=[]                # 横式列表矩阵
stri=''                 # 存储从横式列表矩阵临时提取的字符
vertical=[]             # 纵式列表矩阵
for item in chart:                           # 遍历4大互联网公司市值列表
    hchartwid = int(item[1] / hchartall)      # 按单位长度计算各公司条形图比较数据
    datazip.append(hchartwid)                 # 添加条形图数据到比较数据列表
maxdata=max(datazip)                          # 获取数据比较列表的最大值
for item in datazip:           # 遍历数据比较列表
   # 转换为1和0组成横式列表矩阵，列表前面的值为1（比较数据大小决定），后面补充0
    horiz.append('1' * int(item) + (maxdata-int(item))*'0')
for i in range(maxdata):         # 按数据比较列表的最大值转换纵式矩阵列表
    for item in horiz:           # 遍历横式矩阵列表
        stri=stri+item[maxdata-i-1]   # 提取每个列表的一个字符
    vertical.append(stri)         # 添加到纵式列表
    stri=''                       # 清空临时存储的横式数据
print('\33[35m',chart[0][1],' ',chart[1][1],' ',chart[2][1],' ',chart[3][1],'\33[0m')
for item in vertical:           # 遍历列表矩阵
    for i in item:              # 遍历其中一个列表
        if i=='1':              # 如果为“1”，输出背景色
            print('  \033[41m'+'   '+ '\033[0m',end='  ')
        else:                  # 如果为“0”，不输出内容
            print("     ",end='  ')
    print()                     # 输出间隔列
print(chart[0][0],chart[1][0],chart[2][0],chart[3][0] )  # 输出公司名称
