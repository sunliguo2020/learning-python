from turtle import *
import turtle
from random import randint
import sys
#屏幕初始化
screen = turtle.Screen()
screen.title("幸运大转盘 转转转~")
screen.setup(480,450)
screen.bgpic("转盘.png")         #背景图片
screen.delay(0)
#制定点位置
list1 = ((8,30),(20,50),(0,120),(-20,50),(-8,30))
screen.addshape("myarrow",list1)   #添加自定义形状 
#绘制箭头
arrow = Turtle(shape = "myarrow")
arrow.color("purple")          #定义箭头颜色
arrow.rt(0)                    #初始化箭头位置
rotateNumber = randint(50,100) #随机产生旋转次数50-100之间
angle = 45                     #定义每次旋转45度
def rotate():
    global rotateNumber,angle
    screen.onkeypress(None,"space")  #按空格键启动转盘
    if rotateNumber>0:               #rotateNumber非0时转动
        if rotateNumber<20:
           angle = rotateNumber      #rotateNumber小于20旋转角度变小（减速）
        arrow.rt(angle)              #向右旋转angle度
        rotateNumber = rotateNumber - 1
        screen.ontimer(rotate,20)    #计时器（每隔20秒调用一次rotate）
    else:                            #rotateNumber为0停止转动
        rotateNumber = randint(50,100)     #随机产生旋转次数50-100之间
        angle = 45                         #定义每次旋转45度
        screen.onkeypress(rotate,"space")  #按空格键启动转盘
        
screen.onkeypress(rotate,"space")          
screen.listen()        #开启监听，将鼠标定位到画布
screen.mainloop() 
