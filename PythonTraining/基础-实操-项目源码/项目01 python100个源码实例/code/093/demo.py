import  random
import  os
randstr=[]
def mkpath(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)
incount=input(" 请输入生成防伪码数量:")
while int(incount) <= 0:  # 如果输入数量小于等于0,则要求重新输入
    incount = input(" 请重新输入生成防伪码数量:")
for j in range(int(incount)):   # 根据输入数量循环生成防伪码
    randfir = ''       # 设置存储单条注册码的变量为空
    for i in range(6):  # 循环生成单条注册码
        randfir = randfir + str(random.randint(0,9))  # 产生数字随机因子　
    randfir = randfir + "\n"   # 在单条注册码后面添加转义换行字符"/n"，使验证码单条列显示　
    randstr.append(randfir)    # 将单条注册码添加到保存批量验证码的变量randstr　
datapath = os.getcwd()
datapath = datapath + "\code"
mkpath(datapath)
datafile = datapath + "\\scode5.txt"
file = open(datafile, 'w')
pdata = ""
wdata = ""
for i in range(len(randstr)):
    wdata = str(randstr[i].replace('[', '')).replace(']', '')
    wdata = wdata.replace(''''','').replace(''''', '')
    file.write(str(wdata))
    pdata = pdata + wdata
file.close()
print( pdata )
print( "生成的6位防伪码保存在",datapath )
