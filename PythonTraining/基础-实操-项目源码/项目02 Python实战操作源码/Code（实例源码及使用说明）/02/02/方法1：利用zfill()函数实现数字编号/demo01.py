# *_* coding : UTF-8 *_*

# 文件名称   ：demo01.py
# 开发工具   ：PyCharm

datasort = []
i = 0
data = '莱科宁 236,汉密尔顿 358,维泰尔 294,维斯塔潘 216,博塔斯 227'    # 字符串数据
newlist = data.split(',')                                              # 将字符串数据分割为列表
print(newlist)
# 将车手与积分数据添加到新的列表中
for item in newlist:
    opendata = item.split(' ')
    datasort.append([opendata[1], opendata[0]])
datasort.sort(reverse=True)                                            # 数据降序排列
print("\033[1;34m=" * 35)
print("输出F1大奖赛车手积分".center(25))
print('=' * 35 + '\033[0m')
print('排名        车手             积分')
# 循环打印每个赛车手与对应积分
for item in datasort:
    i = i + 1
    print('\033[1;32;41m ' + str(i).zfill(2) + ' \033[0m    ', item[1].ljust(14) + '\t', item[0].ljust(6) + '\t')
    print()
