# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/7 8:27
"""


def multiply(*numbers):
    print(numbers)
    print(*numbers)
    print(type(numbers))
    result = 1

    for n in numbers:
        result = result * n
    return result


print(multiply(10, 100))

print("*"*100)
def function(a,b,*args,keyword=True,**kwargs):
    print(a,b)
    print(args)
    print(keyword)
    print(kwargs)

d = {"param_a":43,"param_b":44}
function(1,2,*[5,3,4],param=42,*d)
