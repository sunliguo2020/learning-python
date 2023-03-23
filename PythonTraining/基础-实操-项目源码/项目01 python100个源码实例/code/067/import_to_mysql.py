import pymysql
import xlrd

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='flask', charset='utf8')
cursor = conn.cursor() # 创建游标

# 读取excel中内容到数据库
workbook = xlrd.open_workbook('./明日学院Python课程数据2019-09-25.xlsx')
sheet = workbook.sheet_by_index(0) # 根据索引获取sheet
data_list = []
nrows = sheet.nrows  # 获取行数
ncols = sheet.ncols  # 获取列数

# 遍历每一行数据
for i in range(1, nrows):
    # 在列表中第一个元素为0，方便后面使用insert插入数据
    row_values = [0]+ sheet.row_values(i)
    # 如果折扣价不存在，设置为None
    if not row_values[9]:
        row_values[9] = None
    # 如果折扣率不存在，设置为None
    if not row_values[10]:
        row_values[10] = None
    # 追加到列表中
    data_list.append(row_values)

# 拼接'%s'
val = '%s,'*(ncols+1)
# 批量添加数据
cursor.executemany(f"insert into course values({val[:-1]});", data_list)
conn.commit()   # 提交数据
cursor.close()  # 关闭游标
conn.close()    # 关闭数据库连接