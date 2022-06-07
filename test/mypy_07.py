"""
测试参数的传递
1.对“可变参数”进行“写操作”，直接作用于本身
2.对“不可变参数”进行“写操作”，会产生一个新的“对象空间”，并用新的值填充这块空间。
传递可变参数
"""
a=100
b=[10,20]

def test01(m):
    print("start function test01","#"*10)
    print("m:",id(m))
    m.append(30)

    print("end function test01","$"*10)

def test02(n):
    print("start test02","#"*10)
    print("id(n):",id(n))
    n=999
    print("n=", n)
    print("id(n)",id(n))

    print("end test02","$"*10)



print("a=",a)
print("id(a)",id(a))


print("b=",b)
print("id(b)",id(b))

test02(a)
test01(b)
print(b)
print(a)