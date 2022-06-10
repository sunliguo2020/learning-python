
from functools import reduce

a = [1,2,3,4,5,6,7,8,9,10]
b = list(range(1,101))

def add(x,y):
    return x+y
print(reduce(add,a))
print(reduce(add,b))