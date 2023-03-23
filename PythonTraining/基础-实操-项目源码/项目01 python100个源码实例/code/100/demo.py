go=""
out=''
with open('ques.txt','r') as file:             # 打开听写源文件
    word = file.readlines()                # 读取全部信息到列表
list=[i for i in word if i!="\n"]             # 去除列表中的空行       
new=[i.replace('\n','') for i in list]          # 去除每个元素中的‘\n’ 
for (i, item)in enumerate(new,1) :
    mmm=item.split(".")
    if len(mmm)>1:
        go+=format(i,"0>3")+"  "+ mmm[1].strip(" ")+"\n"
        sss=mmm[1].split("：")
        out+=format(i,"0>3")+ "  "+sss[0].strip(" ")+"\n"
    else:
        go+=item
print(go)
print()
print()
print(out)
