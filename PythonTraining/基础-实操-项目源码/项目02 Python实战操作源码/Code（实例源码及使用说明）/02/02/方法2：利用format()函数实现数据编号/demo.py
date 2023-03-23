# *_* coding : UTF-8 *_*
# 文件名称   ：demo.py
# 开发工具   ：PyCharm

nba=['猛龙','勇士','雄鹿','开拓者','掘金','76人']   # 数据列表
i=0                                                 # 默认编号
for item in nba:
    i=i+1                                           # 递增编号
    data='{:0>2}'.format(i)+ '   '+  item           # 数字补0，填充左边宽度为2
    print(data)                                     # 打印带编号的数据
