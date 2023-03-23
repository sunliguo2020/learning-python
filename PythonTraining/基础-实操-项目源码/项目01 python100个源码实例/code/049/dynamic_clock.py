'''
动态时钟
'''
import turtle                 # 导入绘图海龟模块
import datetime               # 导入日期时间模块

# 移动一段距离
def skip(distance):          # 移动方法，不留移动痕迹
    turtle.penup()           # 抬笔不绘制
    turtle.forward(distance) # 移动指定距离
    turtle.pendown()         # 落笔移动绘制

def draw_clock_dial():            # 绘制表盘的方法
    turtle.reset()           # 删除图形归位
    turtle.hideturtle()       # 隐藏箭头
    for i in range(60):       # 循环执行60次，一圈为360度所以每一秒的角度为6度
        skip(160)              # 移动160，相当于表盘圆的半径
        # 每5秒绘制一个小时刻度
        if i % 5 == 0:
            turtle.pensize(7)       # 刻度大小
            # 画时钟
            turtle.forward(20)       # 小时刻度的长度为20
            # if i == 0:               # 判断第一个位置为12点
            #     # 写入数字12
            #     turtle.write(12, align='center', font=('Courier', 14, 'bold'))
            # elif i == 25 or i == 30 or i == 35:    # 5、6、7
            #     skip(25)   # 避免与刻度重叠，所以多移动一段距离
            #     # 根据i除以5获取，5点、6点、7点并写入对应的数字
            #     turtle.write(int(i/5), align='center', font=('Courier', 14, 'bold'))
            #     skip(-25)  # 回到原位置
            # else:
            #     # 根据i除以5获取其它时间的数字并写入
            #     turtle.write(int(i/5), align='center', font=('Courier', 14, 'bold'))
            skip(-20)      # 复原小时刻度的位置
        else:
            turtle.pensize(1)      # 将画笔大小设置为1
            turtle.dot()           # 绘制分钟刻度的小圆点
        skip(-160)                 # 回到中心位置
        turtle.right(6)            # 向右旋转6度


def get_week(t):                   # 获取星期的方法
    week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return week[t.weekday()]       # 返回当天的星期


def create_pointer(length, name):     # 创建指针方法
    turtle.reset()                 # 删除图形归位
    skip(-length * 0.1)            # 抬笔移动指定距离
    turtle.begin_poly()            # 记录多边形
    turtle.forward(length * 1.1)   # 绘制指定长度的指针
    turtle.end_poly()              # 停止记录多边形
    # 注册多边形状
    turtle.register_shape(name, turtle.get_poly())

def init_pointer():                # 初始化指针
    global secHand, minHand, hurHand, printer
    turtle.mode("logo")              # 重置Turtle指向上
    create_pointer(135,"secHand")       # 创建秒针图形
    create_pointer(110,"minHand")       # 创建分针图形
    create_pointer(90,"hurHand")        # 创建时针图形
    secHand = turtle.Turtle()        # 创建秒针turtle对象
    secHand.shape("secHand")         # 创建指定秒针名称的形状
    minHand = turtle.Turtle()        # 创建分针turtle对象
    minHand.shape("minHand")         # 创建指定分针名称的形状
    hurHand = turtle.Turtle()        # 创建时针turtle对象
    hurHand.shape("hurHand")         # 创建指定时针名称的形状
    for hand in secHand, minHand, hurHand:   # 循环遍历三个指针
        hand.shapesize(1, 1, 5)              # 设置形状拉伸大小和轮廓线
        hand.speed(0)                        # 设置速度为最快
    printer = turtle.Turtle()                # 创建绘制文字的Turtle对象
    printer.hideturtle()                     # 隐藏箭头
    printer.penup()                          # 抬笔

def move_pointer():                          # 移动指针的方法
    # 不停的获取时间
    t = datetime.datetime.today()
    second = t.second + t.microsecond * 0.000001    # 计算移动的秒
    minute = t.minute + second/60                   # 计算移动的分
    hour = t.hour + minute/60                       # 计算移动的小时
    secHand.setheading(6*second)                     # 设置秒针的角度
    minHand.setheading(6*minute)                     # 设置分针的角度
    hurHand.setheading(30*hour)                      # 设置时针的角度
    turtle.tracer(False)                             # 关闭绘画效果
    printer.forward(65)                              # 向上移动65
    # 绘制星期
    printer.write(get_week(t), align="center",font=("Courier", 14, "bold"))
    printer.back(130)                                # 倒退130
    # 绘制年月日
    printer.write(t.strftime('%Y-%m-%d'), align="center",font=("Courier", 14, "bold"))
    printer.home()                                   # 归位
    turtle.tracer(True)                              # 开启绘画效果
    turtle.ontimer(move_pointer, 10)                 # 10毫秒后调用move_pointer()方法

if __name__ == '__main__':
    turtle.setup(450, 450)      # 创建窗体大小
    init_pointer()              # 调用初始化指针的方法
    turtle.tracer(False)        # 关闭绘画效果
    draw_clock_dial()            # 绘制表盘
    move_pointer()               # 调用移动指针的方法
    turtle.mainloop()            # 不关闭窗体
