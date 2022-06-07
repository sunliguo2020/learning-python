a = [1,2,3,4,5,6]
from collections import Iterator

result=map(str,a)
print(list(result))

b = [10,20,30]

# print(list(map(str,a,b)))
def add(x,y):
    return x+y
print(list(map(add,a,b)))

print(isinstance(map(str,a),Iterator))