import random
num = []                                # 用于存放抽奖码
# 将抽奖码添加到num中
for i in range(12):
    prizenum = input("请输入第" + str(i + 1) + "个抽奖码：")
    num.append(prizenum)
resultList = []                         # 用于存放随机数结果
# 生成随机数的递归数学，参数counter表示当前准备要生成的第几个有效随机数
def generateRand(counter):
    tempInt = random.randint(0, 11)     # 生成一个范围内的临时随机数
    if(counter <= 5):                   # 先看随机数的总个数是不是够了，如果不够
        if(tempInt not in resultList):  # 再检查当前已经生成的临时随机数是不是已经存在
            resultList.append(tempInt)  # 如果不存在，则将其追加到结果resultList中
            counter += 1                # 然后将表示有效结果的个数加1
        generateRand(counter)           # 不管上面的if是否成立，都要递归。
generateRand(1)                    # 调用递归函数，并给当前要生成的有效随机数的个序号置为1
prize = []                              # 用于存放中奖号码
# 将中奖号码添加到结果prize中
for j in range(5):
    prize.append(num[resultList[j]])
print("\n中奖号码：")           # 输出中奖结果
for k in range(5):
    print(prize[k], end="\t")
