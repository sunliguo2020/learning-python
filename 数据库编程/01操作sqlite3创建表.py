import sqlite3

conn = sqlite3.connect('./sqlit3_1.db')
print(conn)

cur = conn.cursor()
sql = """create table t_person(pno integer primary key ,pname varchar not null,age integer)"""
try :
    cur.execute(sql)
    print("创建表成功")
except Exception as e:
    print("创建表失败",e)
finally:
    cur.close()
    conn.close()