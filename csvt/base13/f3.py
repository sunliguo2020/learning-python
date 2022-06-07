def f():
    global v1
    v1 = 'a'
    print "in f()",id(v1)


#v1 = 'in global var'

print v1,id(v1)

f()

