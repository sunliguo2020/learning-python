# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/7/12 16:11
<<<<<<< HEAD
"""
import pymysql
import math
=======
2022-07-21:发现一个问题:
                    第一次查询的是全部的数据，然后轮询这些数据，在第二次删除不是第一次的数据。
                    但是删除后，第一次的数据还有，这就把不该删除的都删除了。

"""
import pymysql
import math
import logging


logging.basicConfig(filename='del_dump_mysql.log',
                    level=logging.DEBUG,
                    filemode='a',
                    encoding='utf-8',
                    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(message)s')
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc


def get_data_from_mysql(table=''):
    conn = pymysql.Connect(host='192.168.1.207',
                           user='root',
                           password='admin',
                           database='ziliao',
                           port=3306)
    cur = conn.cursor()
    # 获取数据库的总行数
    sql = f'select count(1) from `{table}`;'
    cur.execute(sql)
    counts = cur.fetchone()
    # print(counts)
    per = math.ceil(counts[0] / 5000) + 1
    # print(per)

    for i in range(0, per):
        sql = f'select `id`,`idcard`,`personid` from `{table}` order by `mod_time` DESC limit {i * 5000},5000 ;'
        cur.execute(sql)
        inner_result = cur.fetchone()
        while inner_result:
            yield inner_result
            inner_result = cur.fetchone()


if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< HEAD
    conn2 = pymysql.Connect(host='192.168.1.207',
                           user='root',
                           password='admin',
                           database='ziliao',
                           port=3306)
    cur2 = conn2.cursor()
    for i in get_data_from_mysql('PersonalId'):
        id, idcard, personid = i
        if personid is None:
            sql1 = f'delete from `PersonalId` where id !={id} and idcard="{idcard}" and personid is Null '
        else:
            sql1 = f'delete from `PersonalId` where id !={id} and idcard="{idcard}" and personid="{personid}" '
        print(sql1)
=======
=======
    count = 0
>>>>>>> 44cd2abc499f1b697db5f17c13be08680ed0ce00
    table = 'PersonalId'
    conn2 = pymysql.Connect(host='192.168.1.207',
                            user='root',
                            password='admin',
                            database='ziliao',
                            port=3306)
    cur2 = conn2.cursor()
    for i in get_data_from_mysql('PersonalId'):
        count +=1
        print(f"count:{count}")
        id, idcard, personid = i
        #
        # 先查询这条数据是否已经删除
        check_sql = f"select * from {table} where id = {id}"
        cur2.execute(check_sql)
        result = cur2.fetchone()
        if result is None:
            print(f"{id},{idcard},{personid} 该条记录已经删除了。")
            logging.debug(f"{id},{idcard},{personid} 该条记录已经删除了。")
            continue
        #personid是否为空时，sql语句不同。
        if personid is None:
            sql1 = f'delete from `PersonalId` where id <> {id} and idcard="{idcard}" and personid is Null '
        else:
            sql1 = f'delete from `PersonalId` where id <> {id} and idcard="{idcard}" and personid="{personid}" '
        print(sql1)

>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
        cur2.execute(sql1)
        print(f"删除的个数:{cur2.rowcount}")
        # break
