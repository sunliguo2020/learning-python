from machine import Pin, SoftI2C
from time import sleep
from oled import ssd1306


# 创建i2c对象
i2c = SoftI2C(scl=Pin(18), sda=Pin(23))

# 宽度高度
oled_width = 128
oled_height = 32

# 创建oled屏幕对象
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

if __name__ =="__main__":
    # 在指定位置处显示文字
    oled.text('Hello!', 0, 0)
    oled.text('Hello, World 2!', 0, 10)
    oled.text('Hello, World 3!', 0, 20)
            
    oled.show()
