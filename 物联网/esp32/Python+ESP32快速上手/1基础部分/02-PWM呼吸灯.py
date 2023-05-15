from machine import Pin,PWM
import time

led2 = PWM(Pin(12))
led2.freq(1000)
while True:
    # 从不亮慢慢变亮
    for i in range(0,1024):
        led2.duty(i)
        time.sleep_ms(1)
    # 从亮到慢慢不亮
    for i in range(1023,-1,-1):
        led2.duty(i)
        time.sleep_ms(1)
    