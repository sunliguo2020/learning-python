# *_* coding : UTF-8 *_*

# 文件名称   ：demo01.py
# 开发工具   ：PyCharm
############字符或特殊符号横向条形图输出##################################
# 4大互联网公司市值信息列表
chart = [['alibaba', 4580], ['amazon', 9628], ['apple', 11331], ['oracle', 2053]]
hchartall = 300  # 数据单位长度参数
mark = '$'  # 条形图填充字符为'$'
# mark=chr(0x25a0)                             # 条形图填充字符为方块
horiz = []  # 横式二维列表
for item in chart:  # 遍历列表，转换量化数据为二维列表
    hchartwid = int(item[1] / hchartall)  # 获得条形图量化数据
    horiz.append(item[0].ljust(8) +hchartwid * mark)  # 转换为二维列表
for item in horiz:                       # 遍历输出条形图
    print( '  \033[1;31;0m ' + item + '\033[0m')
for item in chart:                            # 遍历列表
    hchartwid = int(item[1] / hchartall)      # 获得条形图比较数据
    print( item[0].ljust(8) + '  \033[1;31;0m ' + hchartwid * mark + '\033[0m')
