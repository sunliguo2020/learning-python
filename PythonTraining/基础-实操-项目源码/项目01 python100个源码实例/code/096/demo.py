import os
import random
import qrcode
def mkpath(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)
incount = 0
while int(incount) == 0:
    incount = input("请输入要生成的12位数字二维码数量:")
    mkpath ("qrcode")
    for j in range(int(incount)):
        strone = ''
        for i in range(12):
            strone = strone + str(random.choice(range(9)))
        encoder =qrcode.make(strone)
        encoder.save("qrcode\\" + strone + ".png")
