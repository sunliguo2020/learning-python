import machine
import time


a = machine.Pin(13, machine.Pin.OUT)
b = machine.Pin(12, machine.Pin.OUT)
c = machine.Pin(18, machine.Pin.OUT)
d = machine.Pin(27, machine.Pin.OUT)
e = machine.Pin(26, machine.Pin.OUT)
f = machine.Pin(19, machine.Pin.OUT)
g = machine.Pin(33, machine.Pin.OUT)
dot = machine.Pin(32, machine.Pin.OUT)

number_led = [a, b, c, d, e, f, g, dot]

number_dict = {
    0: "11111100",
    1: "01100000",
    2: "11011010",
    3: "11110010",
    4: "01100110",
    5: "10110110",
    6: "10111110",
    7: "11100000",
    8: "11111110",
    9: "11110110",
    "open": "11111111",
    "close": "00000000"
}

def show_number(number):
    if number_dict.get(number):
        i = 0
        for bit in number_dict.get(number):
            if bit == "1":
                number_led[i].value(1)
            else:
                number_led[i].value(0)
            i += 1

def main():
    show_number("open")  # 全亮
    #show_number("close")  # 全灭
    #show_number(1)
    
    time.sleep(2)
    for i in range(10):
        show_number(i)
        time.sleep(0.3)

if __name__ == "__main__":
    main()

