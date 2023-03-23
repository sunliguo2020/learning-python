import random
#定义多个变量并赋值
exp1,exp2 = "",""
str1,str2 = "",""
j=0
count=int(input("请输入出题数量："))
while j<count:
    if j<count:                              # 随机产生"+"或 "-"号
        flag = random.choice(["+", "-"])   # 随机产生"+"或 "-"号
        if flag == "+":
            a = random.randint(0, 100)
            b = random.randint(0, 100-a)
            result=a+b
        # 如果是减法，被减数和减数都应小于100
        else:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            # ab比较，较大的数为被减数
            if a < b:
               a,b=b,a
            result=a-b
        a = str(a).ljust(2, " ")       # ljust左对齐
        b = str(b).ljust(2, " ")
        exp1 = a +" "+ flag +" "+ b + " ="
        exp2 = a +" "+flag +" "+ b + " ="+str(result)
        if j%2==0:                       #  j为偶数，不换行
            str1 = str1 + exp1 + '\t'
            str2 = str2 + exp2 + '\t'        
        else:                              #  j为奇数，换行
            str1 = str1 + exp1 + '\n'
            str2 = str2 + exp2 + '\n'
        j=j+1
with open('math.txt','w') as f:
    f.write(str1)
with open('key.txt','w') as f:
    f.write(str2)
print(count,"道混合加减法题：")    
print(str1)
print(count,"道混合加减法题（带答案）：")  
print(str2)
