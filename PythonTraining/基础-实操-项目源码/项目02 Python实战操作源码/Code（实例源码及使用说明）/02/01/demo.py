# *_* coding : UTF-8 *_*
# 文件名称   ：demo.py
# 开发工具   ：PyCharm

menu = '球员               球队      总得分    场均得分    总篮板    场均篮板'      # 项目菜单
cba = []                                  # 该列表用于保存处理后的数据
for line in open('cba.txt'):
    new = line.replace('\t', ',')         # 将每行数据中的“\t”替换为“,”
    over = new.replace('\n', '')          # 通过替换的方式去除换行符“\n”
    list1 = over.split(',')               # 将每行数据转换为列表
    cba.append(list1)                     # 将每行数据添加至cba列表
##print(cba)
print("\033[1;35m=" * 70)
print('2018-2019赛季CBA 常规赛得分榜'.center(60))
print('=' * 70 + '\033[0m')
print(menu)
for item in cba:
    len1 = len(item[0].encode("gbk")) - len(item[0])    # 计算球员名字长度
    item11 = item[0].ljust(18 - len1)                   # 计算显示球员名字与球队之间的距离
    len2 = len(item[1].encode("gbk")) - len(item[1])    # 计算球队名称的长度
    item12 = item[1].ljust(10 - len2)                   # 计算显示球队名称与总得分之间的距离

    '''实现对齐的代码'''
    # 根据指定距离打印信息
    temp = "print('{: <"+ str(18 - len1)+"}'.format(item11),'{: <"+ str(10 - len2)+"}'.format(item12),'{: <"+ str(10)+"}'.format(item[2])," \
         "'\033[1;31m' + '{: <"+ str(10)+"}'.format(item[3]) + '\033[0m','{: <"+ str(10)+"}'.format(item[4]),'{: <"+ str(10)+"}'.format(item[5]))"
    exec(temp)
    '''未对齐的代码
    print('{: <18}'.format(item11),'{: <10}'.format(item12),'{: <10}'.format(item[2])," \
         "'\033[1;31m' + '{: <10}'.format(item[3]) + '\033[0m','{: <10}'.format(item[4]),'{: <10}'.format(item[5]))
    '''
