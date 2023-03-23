import tushare as ts
df = ts.get_hist_data('000001')
#直接保存
df.to_csv('000001.csv')
#df.to_excel('000001.xls')
#设定数据位置（从第3行，第6列开始插入数据）
#df.to_excel('c:/day/0001.xlsx', startrow=2,startcol=5)
#df.to_csv('000001.csv')




