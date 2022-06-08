a=3

def test01():
    """
    doc

    :return:
    """
    b=4
    #print(a)
    global a
    a=333
    print(b*10)
    print(locals())
    print(globals())
#print(a)

test01()
print(a)