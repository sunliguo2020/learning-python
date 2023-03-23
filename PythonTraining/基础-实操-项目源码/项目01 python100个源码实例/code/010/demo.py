print('RGB模式十进制颜色与十六进制颜色转换'.center(55))
print('='*60)
def rgbhex(rgbr,rgbg,rgbb):
    return hex(int(rgbr)).replace('0x','')+hex(int(rgbg)).replace('0x','') +hex(int(rgbb)).replace('0x','')
r=input('请输入定位点RGB颜色值的R值,取值范围0--255！')
g=input('请输入定位点RGB颜色值的G值,取值范围0--255！')
b=input('请输入定位点RGB颜色值的B值,取值范围0--255！')
print('该定位点的16进制颜色值为',rgbhex(r,g,b) )
