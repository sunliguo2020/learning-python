gdp='广东:97277.77:107671.07 江苏:92595.40:99631.52 山东:76469.70:71067.5 浙江:56197.00:62353 河南:48055.90:54259.2 四川:40678.10:46615.82 湖北:39366.60:45828.31 湖南:36425.78:39752.12 河北:36010.30:35104.5 福建:35804.04:42395'
dict={}
list=[]
base=3000
new=gdp.split(" ")
for item in new:
    list=item.split(":")
    dict.update({list[0]:[list[2],list[1]]})
up=sorted(dict.items(),key=lambda x:float(x[1][0]),reverse=False)
for item in up:
    lenb=format(float(item[1][0])/base,".0f")
    print(item[0].ljust(4)+ "\t"+int(lenb) * chr(9632) + "  2019年GDP:" + str(item[1][0]))
    lenb=format(float(item[1][1])/base,".0f")
    print("".ljust(4)+ "\t"+int(lenb) * chr(9632) + "  2018年GDP:" + str(item[1][1]))
