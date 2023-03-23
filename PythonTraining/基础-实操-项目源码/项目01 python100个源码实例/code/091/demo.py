print("\033[1;31;47m     市政务中心排队系统     \033[0m ")
i=2001
j=0
order="①②③④⑤①②③④⑤"
print("\033[1;31;47m 请%d"% i  +"号用户  到"+order[j]+ "号窗口办理  \033[0m ")
i=i+1
j=j+1
print("\033[1;31;47m 请%d"% i  +"号用户  到"+order[j]+ "号窗口办理  \033[0m ")
i=i+1
j=j+1
print("\033[1;31;47m 请%d"% i   +"号用户  到"+order[j]+ "号窗口办理  \033[0m ")
i=i+1
j=j+1
print("\033[1;31;47m 请%d"% i   +"号用户  到"+order[j]+ "号窗口办理  \033[0m ")
i=i+1
j=j+1
print("\033[1;31;47m 请%d"% i   +"号用户  到"+order[j]+ "号窗口办理  \033[0m ")
while True:
    str=input("回车自动叫号")
    if str=='q'or str=='Q':
        break
    else:
        i=i+1
        j=j+1
        print("\033[1;31;47m 请%d"% i   +"号用户  到"+order[j]+ "号窗口办理  \033[0m ")
