# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/21 15:38
"""
import pandas as pd
import pymysql
from flask import Flask

app = Flask("网页展示Mysql")

coon = pymysql.Connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='',
                       db='ziliao')

@app.route('/')
def index():
    sql = 'select * from `sgms_new_replay` limit 1000;'
    df = pd.read_sql(sql, con=coon)
    return df.to_html()


app.run()
