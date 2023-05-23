'''
深圳市普中科技有限公司（PRECHIN 普中）
技术支持：www.prechin.net
PRECHIN
 普中

实验名称：DHT11温湿度传感器实验
接线说明：DHT11温湿度传感器模块-->ESP32 IO
         (VCC)-->(5V)
         (DATA)-->(27)
         (GND)-->(GND)
         
实验现象：程序下载成功后，软件shell控制台间隔2S输出DHT11温湿度传感器采集的温度和湿度
         
注意事项：

'''

#导入Pin模块
from machine import Pin
import time
import dht
from oled.oled import oled

#定义DHT11控制对象
dht11=dht.DHT11(Pin(17))


#程序入口
#if __name__=="__main__":
time.sleep(1)  #首次启动间隔1S让传感器稳定
while True:
    dht11.measure()  #调用DHT类库中测量数据的函数
    temp = dht11.temperature()
    humi = dht11.humidity()
    if temp==None:
        print("DHT11传感器检测失败！")
    else:
        print("temp=%d°C  humi=%dRH" %(temp,humi))
        oled.fill(0)  #清空屏幕
        oled.text(f"temp={temp},humi={humi}",0,0)
        oled.show()
    time.sleep(2)  #如果延时时间过短，DHT11温湿度传感器不工作
