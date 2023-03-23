# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  11:14
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块
import pymysql  # 导入操作mysql模块
import sqlalchemy  # 导入sqlalchemy数据库操作模块

# 使用pymysql连接数据库
pymysql_db = pymysql.connect(host="localhost", user="root",
                             password="root", db="jd_data", port=3306, charset="utf8")
# sql查询语句，查询数据表中前5条书名信息
sql = "select book_name from sales_volume_rankings where id<=5"
# 通过read_sql_query()函数读取数据库信息
sql_query_data = pandas.read_sql_query(sql=sql,con=pymysql_db)
print('通过read_sql_query()函数读取数据库信息如下：\n', sql_query_data)

# 使用sqlalchemy连接数据库,依次设置
# （数据库产品名称+数据库操作模块名://数据库用户名:密码@数据库ip地址：数据库端口号/数据库名称）
sqlalchemy_db = sqlalchemy.create_engine\
    ("mysql+pymysql://root:root@localhost:3306/jd_data")
# 通过read_sql_table()函数读取数据库信息
sql_table_data = pandas.read_sql_table\
    (table_name='sales_volume_rankings', con=sqlalchemy_db)
print('\n通过read_sql_table()函数读取数据库信息长度为：', len(sql_table_data))

# 通过read_sql()函数读取数据库信息
read_sql_data = pandas.read_sql(sql=sql,con=sqlalchemy_db)
print('\n通过read_sql()函数读取数据库信息如下：\n', read_sql_data)
