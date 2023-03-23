
from random import randrange          # 导入随机函数
from freegames import vector,square  # 导入向量函数与绘图函数
import turtle                         # 导入绘图海龟模块

food = vector(0,0)        # 食物
snake = [vector(10, 0)]   # 蛇
position = vector(0, -10) # 移动位置，一步的距离为10

def change(x, y):        # 改变蛇的移动方向
    position.x = x
    position.y = y

def is_inside(head):        # 判断蛇头是否在窗体内
    return -200 < head.x < 190 and -200 < head.y < 190

def move():                   # 可以让蛇移动的方法
    head = snake[-1].copy()    # 确定蛇头的位置
    head.move(position)        # 移动一步
    if not is_inside(head) or head in snake:   # 如果蛇的头部位于边界外或者蛇头在蛇的身体中
        square(head.x, head.y, 9, 'red')     # 绘制红色蛇头，说明游戏结束
        turtle.update()                      # 更新
        return
    snake.append(head)                       # 更新蛇的位置
    if head == food:                      # 如果蛇吃到食物
        print('Snake:', len(snake))       # 根据蛇的长度进行加分
        food.x = randrange(-15, 15) * 10  # 随机生成食物x坐标
        food.y = randrange(-15, 15) * 10  # 随机生成食物y坐标
    else:
        snake.pop(0)            # 移除蛇走过的坐标
    turtle.clear()              # 清空蛇走过的位置
    for body in snake:          # 循环遍历蛇的坐标
        square(body.x, body.y, 9, 'black') # 绘制黑色蛇
    square(food.x, food.y, 9, 'green')     # 绘制绿色食物
    turtle.update()
    turtle.ontimer(move, 100)           # 定时执行move函数

if __name__ == '__main__':                  # 程序入口
    turtle.setup(420, 420, 370, 0)          # 创建窗体大小
    turtle.hideturtle()                     # 隐藏箭头显示
    turtle.tracer(False)                   # 关闭绘画效果
    move()          # 调用让蛇移动的方法
    turtle.listen()                        # 事件监听器
    turtle.onkey(lambda: change(10, 0), 'Right')    # 按键盘右键，蛇向右走
    turtle.onkey(lambda: change(-10, 0), 'Left')    # 按键盘左键，蛇向左走
    turtle.onkey(lambda: change(0, 10), 'Up')       # 按键盘上键，蛇向上走
    turtle.onkey(lambda: change(0, -10), 'Down')    # 按键盘下键，蛇向下走
    turtle.done()   # 停止画笔绘制，但绘图窗体不关闭