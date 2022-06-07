def funOut(num1):
    def funIn(num2):
        nonlocal num1
        num1 += 10
        return num1 + num2

    return funIn


f = funOut(100)
print(f(200))
