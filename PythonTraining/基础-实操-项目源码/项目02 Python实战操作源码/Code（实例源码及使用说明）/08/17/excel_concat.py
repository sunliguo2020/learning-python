import pandas as pd
import numpy as np
import glob

filearray=[]
#filelocation=glob.glob(r'F:\1 我的程序\Python程序\aaa\*.xls')
filelocation=glob.glob(r'../data/XS/*.xls')
for filename in filelocation:
    filearray.append(filename)

    print(filename)
res=pd.read_excel(filearray[0])
for i in range(1,len(filearray)):
    A=pd.read_excel(filearray[i])
    res=pd.concat([res,A],ignore_index=True,sort=False)
print(res.index)
writer = pd.ExcelWriter('output.xls')
res.to_excel(writer,'sheet1')
writer.save()

