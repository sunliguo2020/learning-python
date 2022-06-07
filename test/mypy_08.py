'''
浅拷贝和深拷贝
'''

import copy

def testCopy():
    a=[10,20,[3,5]]
    b=copy.copy(a)

    print("a:",a)
    print("b:",b)


    print("id(a):",id(a))
    print("id(b):",id(b))

    b.append(33)
    b[2].append(7)
    b[1]=10000

    print("浅拷贝---")

    print("a:", a)
    print("b:",b)

def testDeepCopy():
    a=[10,20,[3,5]]

    b=copy.deepcopy(a)

    print("a:",a)
    print("b:",b)


    print("id(a):",id(a))
    print("id(b):",id(b))

    b.append(33)
    b[2].append(7)

    print("深拷贝---")

    print("a:", a)
    print("b:",b)


#testDeepCopy()

testCopy()