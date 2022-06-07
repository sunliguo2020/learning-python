def f():
    v1 = 'var in function f()'
    g_v1="g_v in function"
    print g_v1,id(g_v1)
    print id "g_v1 in function is %s" % id(g_v1)

g_v1="global var"

f()
print g_v1,id(g_v1)
print "id in glbal is %s" % id(g_v1)
#print v1
