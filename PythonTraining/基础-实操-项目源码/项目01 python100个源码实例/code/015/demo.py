cause = True  # 设置判断网址是否正确的标志变量为真
ip = input('请输入IP地址:\n').strip(' ')
line = ip.split('.')
if len(line) == 4:  # 如果网址按“.”分为4段
    for item in line:  # 对网址各段进行判断
        if item.isdigit():  # 是否为数字
            if int(item) > 255 or int(item) < 0:
                print('IP地址段输入大于255或小于0错误,将退出!!')
                cause = False  # 网址错误，判断网址标志变量为假
                break  # 退出循环
        else:
            print('IP地址段输入非数字错误（只能输入数字或.）,将退出!!')
            cause = False
            break
    if cause == True:
        print('IP地址输入正确!!')
else:
    print('IP地址输入多于或少于4段地址错误,将退出!!')
