import datetime
notes=[]
note={}
file = open('note.txt')         # 以只写模式打开文件
for i in range(10):                # 只显示最近10条便签
    line= file.readline().strip(' ').strip('\n')     # 读取患者信息
    if line== '':              # 如果信息为空
        break                  # 跳出循环
    lines=line.split("&")
    if len(lines[1])>10:
        notes.append(lines[1][0:10]+"----"+lines[0])
    else:
        notes.append(lines[1]+"----"+lines[0])        
file.close()              # 关闭文件
print("\n".join(notes))
print(" ===============便签本============")
while True:
    choice = input("输入数字1写便签，输入数字2查询便签\n输入数字3浏览全部便签，输入“q”退出系统\n")
    if choice.strip("") == 'q':
        print(" 退出电子便签 ")
        break
    if choice.strip("") == '1':
        order = datetime.datetime.now()
        order = format(order, "%Y-%m-%d %H:%M:%S ")
        word = input("")
        note[order] = word
        file = open('note.txt', 'a')  # 以写模式打开文件
        file.write('\n' + order + '&' + word)
        file.close()  # 关闭文件

    elif choice.strip(" ") == '2':
        str = input("请输入要查询的文字：")
        file = open('note.txt')  # 以只写模式打开文件
        for i in range(10):  # 只显示最近10条便签
            line = file.readline().strip(' ').strip('\n')  # 读取患者信息
            if line == '':  # 如果信息为空
                break  # 跳出循环
            if str in line:  # 如果信息为空
                lines = line.split("&")
                print(lines[0])
                print('     ' + lines[1])
        file.close()  # 关闭文件
    elif choice.strip(" ") == '3':
        file = open('note.txt')  # 以只写模式打开文件
        while True:
            line = file.readline().strip(' ').strip('\n')  # 读取便签信息
            if line == '':  # 如果信息为空
                break  # 跳出循环
            lines = line.split("&")
            print(lines[0])
            print('     ' + lines[1])
        file.close()  # 关闭文件
