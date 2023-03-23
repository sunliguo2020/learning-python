# *_* coding : UTF-8 *_*

# 文件名称   ：demo02.py
# 开发工具   ：PyCharm
############横向条形图背景色##################################
chart=[['alibaba',4580],['amazon',9628],['apple',11331],['oracle',2053]]   # 4大互联网公司市值信息
hchartall=300                                 # 数据单位长度参数
color= '41m '                                 # 条形图颜色参数
for item in chart:                           # 遍历列表
    hchartwid = int(item[1] / hchartall)      # 获得条形图量化数据
    print( item[0].ljust(8) + '  \033[1;32;' +color  + ''.ljust(hchartwid)+ '\033[0m')
    print('')                                 # 条形图之间实现间隔
