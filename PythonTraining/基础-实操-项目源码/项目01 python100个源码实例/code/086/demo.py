import random
list=["春暖花开","十字路口","千军万马","白手起家","张灯结彩","风和日丽","万里长城","人来人往","自由自在","瓜田李下","助人为乐","白手起家","红男绿女","春风化雨","马到成功","拔苗助长","安居乐业","走马观花","念念不忘","落花流水","张灯结彩","一往无前","落地生根","天罗地网","东山再起","一事无成","山清水秀","别有洞天","语重心长","水深火热","鸟语花香","自以为是"]
i=1
count=20
print('直接填写答案，回车进入下一关。什么也不填忽略本成语！！')
while True:
    word= random.choice(list)
    bank= random.randint(0,3)
    new =word[:bank] +"___" +word[bank+1:]      
    print(new)
    num=input("输入：")
    if not num:
        print("过！")
        continue
    elif num.strip(" ")==word[bank]:
        count+=2
        print("正确，你真棒！")
    else:
        count-=2
        print("错了，正确答案：",word[bank])
    i+=1   
    if i>8 :
        break
print("选手最后得分：",count)
