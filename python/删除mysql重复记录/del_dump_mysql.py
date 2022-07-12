# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/7/12 16:11
"""
import pymysql
import math


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
        sql = f'select `id`,`idcard`,`personid` from `{table}` limit {i * 5000},5000;'
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
            sql1 = f'delete from `PersonalId` where id !={id} and idcard={idcard} and personid is Null '
        else:
            sql1 = f'delete from `PersonalId` where id !={id} and idcard={idcard} and personid={personid} '
        print(sql1)
        cur2.execute(sql1)
        print(cur2.rowcount)
        # break
