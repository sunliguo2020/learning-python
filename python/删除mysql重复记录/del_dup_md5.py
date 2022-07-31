# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-07-31 7:27
lost数据表中数据可能在guhua和kuandai中存在
只判断md5sum的值相同，就可以删除lost中的数据库
"""
import pymysql
import math
import logging

logging.basicConfig(filename='del_dump_md5.log',
                    level=logging.DEBUG,
                    filemode='a',
                    encoding='utf-8',
                    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(message)s')


def loop_data_from_mysql(table=''):
    conn = pymysql.Connect(host='127.0.0.1',
                           user='root',
                           password='admin',
                           database='crawl',
                           port=3306)
    cur = conn.cursor()
    # 获取数据库的总行数
    sql = f'select count(1) from `{table}`;'
    cur.execute(sql)
    counts = cur.fetchone()
    # print(counts)
    per = math.ceil(counts[0] / 5000) + 1
    # print(per)

    for i in range(50, per):
        sql = f'select `md5sum` from `{table}` order by `mod_time` DESC limit {i * 5000},5000 ;'
        cur.execute(sql)
        inner_result = cur.fetchone()
        while inner_result:
            yield inner_result
            inner_result = cur.fetchone()


if __name__ == '__main__':
    count = 0
    con2 = pymysql.Connect(host='127.0.0.1',
                           user='root',
                           password='admin',
                           database='crawl',
                           port=3306)
    cur2 = con2.cursor()

    for item in loop_data_from_mysql(table='lost'):
        count += 1
        print(f"{count}:判断{item[0]}")
        md5sum = item[0]
        sql2 = f'select md5sum from `kuandai` where `md5sum` = "{md5sum}"'
        # print(sql2)
        cur2.execute(sql2)
        result = cur2.fetchone()
        print(f'查询返回的值:{result}')

        if result is None:
            continue
        else:
            break
