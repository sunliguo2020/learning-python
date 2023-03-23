import random
print("*****福彩双色球*****")
print("====================")
red=[str(i).zfill(2) for i in (random.sample(range(1,31),6))]
print(','.join(red)+","+str(random.choice(range(1,16))).zfill(2))
import random
print("*****福彩双色球*****")
print("====================")
luck=input("请输入您的幸运数字（1~16）：\n")
inputx=int(input("请输入双色球彩票组数：\n"))
for i in range(inputx):
    red=[str(i).zfill(2) for i in (random.sample(range(1,31),6))]
print(','.join(red)+","+luck.zfill(2))
