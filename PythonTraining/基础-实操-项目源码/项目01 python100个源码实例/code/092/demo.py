import datetime
data = '当前号码:A235,该业务当前等待人数:33,业务类型:个人现金业务'
newlist = data.split(',')
codelist=newlist[0].split(':')
waitlist=newlist[1].split(':')
worklist=newlist[2].split(':')
codeoreder=''.join(codelist[1])
nowcode=codeoreder[0:1]+  str(int(codeoreder[1:4])+1)
waitper=int(''.join(waitlist[1]))+1
print("中国农行银行".center(25))
print( )
print(str(nowcode).rjust(25))
print('   '+worklist[0],':',worklist[1])
print('   '+waitlist[0],':',waitper)
print( 'custom   waiting'.center(25) )
print(  datetime.datetime.today().strftime('%Y-%m-%d   %H:%M:%S').center(25))
print( )
print('过号请重新取号   关门无效')
