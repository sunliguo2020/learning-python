def outer():
    name = "小猿圈，自学编程"
    print(locals())

    def inner(s):
        print("Inner", name)
        print(locals())

    return inner


print(outer())

func = outer()

func("dsf")
