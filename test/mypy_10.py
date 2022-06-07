#使用递归函数，计算阶乘
def f(n):
    if n == 1:
        result = 1
    else:
        result = n*f(n-1)

    return result


print(f(5))