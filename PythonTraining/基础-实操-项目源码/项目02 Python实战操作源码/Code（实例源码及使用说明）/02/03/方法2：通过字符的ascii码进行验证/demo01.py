# *_* coding : UTF-8 *_*
# 文件名称   ：demo01.py
# 开发工具   ：PyCharm

instr=input('请输入5位数字验证码：').strip(' ')   # 获取输入的5位数字
isgo='go'                                         # 是否登录的标记
if len(instr)!=5:                                 # 如果输入的字符（数字）长度不是5时
    print('输入非5位数字，请重新输入！')
    isgo = 'no'
else:
    for i in instr:
        if ord(i) not in range(ord('1'),ord('8')):         # 如果输入字符的ASCII码值为数字字符时
            print('输入了非数字字符，请重新输入！')
            isgo = 'no'
            break
if isgo =='go':                                             # 验证成功输出登录
    print('正在登录站长之家系统！')
