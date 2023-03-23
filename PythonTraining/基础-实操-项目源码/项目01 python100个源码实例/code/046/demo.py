import random
dict_film={}
list_film=[]
file = open('film.txt')  # 以只写模式打开电影及主要演员文件
while True:
    line = file.readline().strip(' ').strip('\n')  # 读取电影及演员信息
    if line == '':  # 如果信息为空
        break  # 跳出循环
    filmline = line.split(":")  # 分解电影与主要演员信息
    list_film.append(filmline[0])

    list_acter = filmline[1].split(',')  # 分解主要演员信息到列表
    dict_film[filmline[0]] = list_acter  # 把电影和主要演员信息添加到字典
file.close()  # 关闭文件
file = open('acter.txt')  # 以只写模式打开文件
while True:
    line = file.readline().strip(' ').strip('\n')  # 读取所有演员信息
    if line == '':  # 如果信息为空
        break  # 跳出循环
    actall = line.split(",")  # 分解演员信息
file.close()  # 关闭文件
film=random.choice(list_film)         # 随机选择电影
acter=dict_film.get(film)             # 根据电影获取主演演员库，用于判断是否为本部电影演员
count=30                              # 竞猜起始分数为30分
print("电影:",film)
print('判断演员是否本部电影的演员。回车确认“是”，输入任意键确认“不是”')
for i in range(6):                     # 6次竞猜
    new = random.choice(actall)        # 随机选择演员
    actall.remove(new)                 # 从演员库删除选择的演员，防止下次再次出现
    print(new)  # 显示竞猜演员
    num = input("").strip()  # 用户进行判断，选择回车还是其他键
    if not num:  # 选择回车，确认是该部电影主演
        if new not in acter:  # 如果该演员不在本部电影主演库里面
            count -= 3  # 积分减3分
            print("答错了，减三分！")
        else:  # 答对了
            count += 3  # 积分加3分
            print("答对了，加三分！")
        print("当前分数：", count)
    else:  # 选择其他键，确认不是该部电影主演
        if new not in acter:  # 如果该演员不在本部电影主演库里面
            count += 3  # 积分加3分
            print("答对了，加三分！")
        else:  # 答错了
            count -= 3  # 积分减3分
            print("答错了，减三分！")
        print("当前分数：", count)  # 输出当前积分

else:
    print("竞猜最高分为48分，你的最后分数：", count)
