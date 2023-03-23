import os
import random
def mkpath(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)
def wfile(sstr, sfile, smsg):
    datapath = os.getcwd()
    datapath = datapath + "\codepath"
    mkpath(datapath)
    datafile = datapath + "\\" + sfile
    file = open(datafile, 'w')
    wrlist = sstr
    fs = sfile
    pdata = ""
    wdata = ""
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[', '')).replace(']', '')
        wdata = wdata.replace(''''','').replace(''''', '')
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print(pdata )
def ffcode(scount, typestr):    # 生成带分析功能的防伪码函数
    letterone = ""
    lettertwo = ""
    for j in range(int(scount)):          # 根据输入防伪码数量生成二维码
        strpro = typestr[0].upper()       # 第一个字母，代表大类，转为大写
        strtype = typestr[1].upper()      # 第二个字母，代表细分类，转为大写
        strclass = typestr[2].upper()     # 第三个字母，版本，转为大写
        randfir = random.sample('1234578', 2)    # 随机产生二个位置放置后两个分析码
        randsec = sorted(randfir)                # 对二个位置排序，以便按序放置分析码
        letterone = ""
        for i in range(6):                       # 随机生成6位数字码
            letterone = letterone + str(random.choice(range(9)))
         # 防伪码第一位是第一个字母，后两个字母的位置根据产生的位置和数字确定
        sim =  strpro + str(
            letterone[0:int(randsec[0])]) + strtype + str(
            letterone[int(randsec[0]):int(randsec[1])]) + strclass + str(letterone[int(randsec[1]):6]) + "\n"
        randstr.append(sim)
        wfile(randstr, typestr + "scode.txt", "生成含数据分析防伪码共计：")
randstr =[]
intype = ""
while not str.isalpha(intype) or len(intype) != 3:
    intype = input("请输入数据分析编号（3位字母）:") # 如ABC,IBM等
incount = 0
while int(incount) <=0 or not incount.isdigit() :
    incount = input("请输入要生成的带数据分析功能的验证码数量:")  
ffcode(incount,intype)    # 生成分析码函数
