from machine import UART
from machine import Pin

import time

uart2 = UART(2, 115200, rx=16, tx=17)

if __name__ == "__main__":
    print('1')
    uart2.write('hello world')
    while True:
        if uart2.any():
            text = uart2.read(128)
            uart2.write(text)
