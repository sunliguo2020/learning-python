import machine
import time

#控制led的GPIO口
led_pin = 12

pin2 = machine.Pin(led_pin, machine.Pin.OUT)
while True:
    pin2.value(1)
    time.sleep(1)
    pin2.value(0)
    time.sleep(1)