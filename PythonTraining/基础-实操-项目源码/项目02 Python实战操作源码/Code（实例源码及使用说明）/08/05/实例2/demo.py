# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/4/19  11:18
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import pandas  # 导入数据统计模块
import sqlalchemy  # 导入sqlalchemy数据库操作模块


# 使用sqlalchemy连接数据库
sqlalchemy_db = sqlalchemy.create_engine\
    ("mysql+pymysql://root:root@localhost:3306/jd_data")
# sql查询语句
sql = "select * from to_sql_demo "
# 模拟写入数据库中的数据
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C':[11,12,13,14,15]}
data__frame = pandas.DataFrame(data)  # 创建DataFrame对象
# 向数据库中写入模拟数据data
data__frame.to_sql('to_sql_demo',sqlalchemy_db,if_exists='append')
# 通过read_sql()函数读取数据库信息
read_sql_data = pandas.read_sql(sql=sql,con=sqlalchemy_db)
print('\n通过read_sql()函数读取数据库信息如下：\n', read_sql_data)
