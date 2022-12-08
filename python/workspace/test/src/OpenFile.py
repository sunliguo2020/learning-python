#_*_coding:utf-8_*_
file = "d:\\test.txtsdfsafdsfsdf"

f = open(file,"a")

#c =f.read()
print  f.tell()
#f.seek(1,2)
f.write("123")

#print f.tell()
#f.write("123445")
#f.write("xxxxx")

print f.tell()
f.seek(0)
#print f.readlines()
f.close()