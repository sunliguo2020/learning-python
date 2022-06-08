# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/2 12:07
"""
import pymysql
from flask import Flask, render_template, request

conn = pymysql.Connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='',
                       db='todo',
                       charset='utf8')


def query_data():
    sql = 'select * from todo_list order by deadline asc'
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(sql)
    return cur.fetchall()


app = Flask("代办项网站")


def insert_to_db(content, deadline):
    sql = f"insert into todo_list (content,deadline) values ('{content}','{deadline}')"
    # print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        content = request.form.get('content')
        deadline = request.form.get('deadline')
        insert_to_db(content, deadline)
    datas = query_data()
    return render_template('index.html', datas=datas)


app.run(debug=True)
