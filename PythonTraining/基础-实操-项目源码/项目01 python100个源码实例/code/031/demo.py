import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
aa ='mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(aa))  #读取Excel数据为dataframe
#定义标签函数
def add_tag(data):
  global tag
  tag=''
  if '零' in data:
      tag ='零基础|'+tag
  if '例' in data:
      tag='实例|'+tag
  if '项目' in data:
      tag='项目|'+tag
  if 'C#' in data:
      tag='C#|'+tag
  if 'Android' in data:
      tag='Android|'+tag
  if 'SQL' in data:
      tag='SQL|'+tag
  if 'Python' in data:
      tag='Python|'+tag
  if 'Oracle' in data:
      tag='Oracle|'+tag   
  return tag
#将添加的标签保存到tag列中
df['tag'] = df['图书名称'].apply(add_tag)
print(df)
#保存数据为excel
df.to_excel('mrbook副本.xlsx')  
