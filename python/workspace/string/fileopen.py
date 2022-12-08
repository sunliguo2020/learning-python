with open('1.txt','r') as f:
    a=f.read()

b="insert into sql "
a=a.replace('\n','\\n')
c=b+'"'+a+'"'
f1 = open('b.txt','w')
f1.write(c)
f1.close()

f2 = open('b.txt','r')
a=f2.read()
print(a.replace('\\n','\n'))