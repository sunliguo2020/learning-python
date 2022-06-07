#测试LEGB

#str="global str"

def outer():
    #str="outer str"
    def inner():
        #str="inner str"
        print(str)

    inner()


outer()