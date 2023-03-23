import turtle    #导入绘图海龟模块

turtle.setup(500,600)    # 设置窗体大小
tree = turtle.Turtle()   # 创建画笔
tree.shape('triangle')   # 默认为三角形
tree.color('green')      # 设置画笔颜色
tree.right(30)           # 向右旋转30度
tree.up()                # 抬起画笔

# 绘制树
def drawing_tree(start,stop,move,is_square=False):
    if is_square:                   # 该参数为True说明绘制树干
        tree.left(30)               # 向左旋转30度
        tree.shape('square')        # 设置绘制物为正方形
        tree.color('brown')         # 设置颜色为棕色
    for r in range(start, stop):    # 循环遍历行的绘制物
        a =r                        # 默认绘制树叶
        if is_square:               # 该参数为True说明绘制树干
            a=1                      # 将a设置为1，只绘制一列图形
        y = 20 * r  # 计算绘制物y坐标的距离
        for c in range(a):  # 循环遍历列的绘制物
            x = 20 * c  # 计算绘制物x坐标的距离
            tree.goto(x, -y + move)  # 移动右半部分的位置
            tree.stamp()  # 复制当前图形，实现绘制
            tree.goto(-x, -y + move)  # 移动左半部分的位置
            tree.stamp()  # 复制当前图形，实现绘制

drawing_tree(1,4,160)          # 绘制圣诞树的前三层
drawing_tree(2,5,120)          # 绘制圣诞树的中间三层
drawing_tree(3,6,80)           # 绘制圣诞树的最后三层
drawing_tree(4,9,40,True)      # 绘制圣诞树的树干

import time                    # 导入时间模块
word = turtle.Turtle()         # 创建绘制文字的画笔对象
word.up()                      # 抬起画笔
word.goto(-150,200)            # 移动到顶部位置
word.color('red')              # 设置画笔颜色为红色
# 写入文字“圣”
word.write("圣",font=(u"黑体",48,"normal"),align="center")
time.sleep(0.5)                # 等待指定时间
word.goto(-50,200)             # 画笔移动至第二个字的位置
# 写入文字“诞”
word.write(arg="诞",move=True,font=(u"黑体",48,"normal"),align="center")
time.sleep(0.5)                # 等待指定时间
word.goto(50,200)              # 画笔移动至第三个字的位置
# 写入文字“快”
word.write("快",font=(u"黑体",48,"normal"),align="center")
time.sleep(0.5)                # 等待指定时间
word.goto(150,200)             # 画笔移动至第四个字的位置
# 写入文字“乐”
word.write("乐",font=(u"黑体",48,"normal"),align="center")
word.hideturtle()       # 隐藏箭头
turtle.mainloop()         # 开始循环防止窗口自动关闭