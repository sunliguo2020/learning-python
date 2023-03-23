# *_* coding : UTF-8 *_*

# 文件名称   ：demo02.py
# 开发工具   ：PyCharm

import random      # 导入随机模块
char=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']    # 随机数据
shop='100000056303'       # 固定编号
prize=[]                  # 保存抽奖号码的列表
inside=''                 # 中段编码
amount = input('请输入购物金额:')     # 获取输入金额
many=int(int(amount)/100)
if int(amount)>=100:
    # 随机生成中段7为编码
    for i in range(0,7):
        if inside=='':
             inside = random.choice(char)
        else:
            inside =inside+ random.choice(char)
    # 生成尾部4为数字，并将组合的抽奖号添加至列表
    for i in range(0,many):
        number = str(i+1).zfill(4)
        prize.append([shop,inside, number])
else:
    print('购物金额低于100元,不能参加抽奖!!!')
print("\033[1;34m=" *24)
print("本次购物抽奖号码")
print('=' *24 +'\033[0m' )
# 打印最终的抽奖号码
for item in prize:
    print(''.join(item))
