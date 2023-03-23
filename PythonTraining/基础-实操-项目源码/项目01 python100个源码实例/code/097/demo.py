from pystrich.ean13 import EAN13Encoder
import os
import random
def mkpath(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)
def scode():
    mainid = input ("请输入EN13的国家代码（3位） : ")         
    while int(mainid) < 1 or len(mainid) != 3:   # 验证输入是否为3位数字
        mainid = inputbox("请输入EN13的国家代码（3位）:")
    compid = input("请输入企业代码（4位）:")  # 输入企业代码
    while int(compid) < 1 or len(compid) != 4:   # 验证输入是否为4位数字
        compid = inputbox("请输入EN13的企业代码（4位）:")
    incount = input("请输入要生成的条形码数量:")
    while int(incount) == 0:   # 输入信息转为整数后等于0，重新输入
        incount = input("请输入要生成的条形码数量:")
    mkpath("barcode")  # 判断保存条形码的文件夹是否存在，不存在，则创建该文件夹
    for j in range(int(incount)):
        strone = ''
        strtwo = ''
        for i in range(5):
            strone = strone + str(random.choice(range(9)))
        barcode=mainid +compid +strone
        print(barcode)
        evensum = int(barcode[0])+int(barcode[2])+ int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + int(barcode[10])  
        oddsum =int( barcode[1])+int(barcode[3])+int(barcode[5])+int(barcode[7])+int(barcode[9]) +int(barcode[11])
        checkbit=int(10-(evensum *3 + oddsum)%10)
        barcode =barcode+str(checkbit)
        print(barcode)
        encoder = EAN13Encoder(barcode)
        encoder.save("barcode\\" + barcode  + ".png")
scode()
