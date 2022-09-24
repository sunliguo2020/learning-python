# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/7/12 16:11

<<<<<<< HEAD

=======
>>>>>>> 5b49079a83b9d5846af2d8ea77afab267c5dc6aa
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


def get_data_from_mysql(table=''):
    """
    @param table:要查询的数据表
    @return:
    """
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

    count = 0

    table = 'PersonalId'
    conn2 = pymysql.Connect(host='192.168.1.207',
                            user='root',
                            password='admin',
                            database='ziliao',
                            port=3306)
    cur2 = conn2.cursor()
    for i in get_data_from_mysql('PersonalId'):
        count += 1
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
        # personid是否为空时，sql语句不同。
        else:
            print(f"result的结果为:{result}")

        if personid is None:
            sql1 = f'delete from `PersonalId` where id <> {id} and idcard="{idcard}" and personid is Null '
        else:
            sql1 = f'delete from `PersonalId` where id <> {id} and idcard="{idcard}" and personid="{personid}" '
        print(sql1)


        cur2.execute(sql1)
        print(f"删除的个数:{cur2.rowcount}")
        if cur2.rowcount > 0:
            logging.debug(f"删除{cur2.rowcount}条记录{sql1} ")
        # break
