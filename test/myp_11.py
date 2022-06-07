#config=utf-8
#测试嵌套函数的定义

def outer():
    print("outer is running ---")

    def inner():
        print("inner is running---")


outer()