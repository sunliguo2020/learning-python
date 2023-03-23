# *_* coding : UTF-8 *_*
# 文件名称   ：demo02.py
# 开发工具   ：PyCharm

instr=input('注册用户名：').strip(' ')      # 获取输入的字符
isgo='go'                                   # 验证成功的标记
for i in instr:                            # 循环判断每个字符的ASCII码值是否合法
    if ord(i) in range(33,127):
        if  ord(i) in  [64,92,47,35]:
             print('输入了非法字符“', i, '”请重新输入！')
             isgo = 'no'
             break
    else:
        print('输入了非法字符,请重新输入！')
        isgo = 'no'
        break

if isgo =='go':                             # 验证成功输出完成注册
    print('用户名注册完成，请继续填写其他注册信息！！')

