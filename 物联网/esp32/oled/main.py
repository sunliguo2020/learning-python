'''
深圳市普中科技有限公司（PRECHIN 普中）
技术支持：www.prechin.net
PRECHIN
 普中

实验名称：OLED液晶显示实验
接线说明：OLED(IIC)液晶模块-->ESP32 IO
         GND-->(GND)
         VCC-->(5V)
         SCL-->(18)
         SDA-->(23)
         
实验现象：程序下载成功后，OLED液晶屏显示字符信息
         
注意事项：

'''

#导入Pin模块
from machine import Pin
import time
from machine import SoftI2C
from oled.ssd1306 import SSD1306_I2C  #I2C的oled选该方法

#创建硬件I2C对象
#i2c=I2C(0,sda=Pin(19), scl=Pin(18), freq=400000)

#创建软件I2C对象
i2c = SoftI2C(sda=Pin(23), scl=Pin(18))
#创建OLED对象，OLED分辨率、I2C接口
oled = SSD1306_I2C(128, 32, i2c) 

#程序入口
if __name__=="__main__":
    oled.fill(0)  #清空屏幕
    oled.show()  #执行显示
    
    oled.text("Hello World!",0,0,1)  #显示字符串
    oled.show()  #执行显示
    
    oled.pixel(10,20,1)  #显示一个像素点
    oled.hline(0,10,100,1)  #画横线
    oled.vline(120,0,30,1)  #画竖线
    oled.line(10,40,100,60,1)  #画指定坐标直线
    oled.rect(50,20,50,30,1)  #画矩形
    oled.fill_rect(60,30,30,20,1)  #画填充矩形
    oled.show()  #执行显示
    
    time.sleep(2)
    oled.fill(0)  #清空屏幕
    oled.text("Hello World!",0,0,1)
    oled.show()  #执行显示
    time.sleep(1)
    
    oled.scroll(10,0)  #指定像素X轴移动
    oled.fill_rect(0,0,10,8,0)  #清除移动前显示区
    oled.show()  #执行显示
    time.sleep(1)
    
    oled.scroll(0,10)  #指定像素Y轴移动
    oled.fill_rect(0,0,128,10,0)  #清除移动前显示区
    oled.show()  #执行显示
    while True:
        pass
        