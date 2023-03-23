from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import datetime
import json


app = Flask(__name__)
# 基本配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:root@localhost/flask'
        )

db = SQLAlchemy(app) # 实例化SQLAlchemy类

# 创建数据表类
class Course(db.Model):
    id = db.Column(db.Integer, autoincrement=True)
    course_id = db.Column(db.BigInteger,nullable=False,unique=True)
    product_name = db.Column(db.String(125), nullable=False)
    provider = db.Column(db.String(125), nullable=False)
    score = db.Column(db.Float(2))
    learner_count = db.Column(db.Integer)
    lesson_count = db.Column(db.Integer)
    lector_name = db.Column(db.String(125))
    original_price = db.Column(db.Float(2))
    discount_price = db.Column(db.Float(2))
    discount_rate = db.Column(db.Float(2))
    img_url = db.Column(db.String(125))
    big_img_url = db.Column(db.String(125))
    description = db.Column(db.Text)

class Sale(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course_id = db.Column(db.BigInteger, db.ForeignKey('course.course_id'))
    product_name = db.Column(db.String(125), nullable=False)
    learner_count = db.Column(db.Integer)
    create_time = db.Column(db.Date, default=datetime.date.today())

    course = db.relationship('Course',
        backref=db.backref('sale', lazy='dynamic'))

class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(125), nullable=False)
    email = db.Column(db.String(125), nullable=False)
    password = db.Column(db.String(125), nullable=False)

@app.route('/course/<int:id>')
def detail(id):
    """
    课程详情
    :param id:
    :return: 课程详细信息
    """
    # 根据课程ID获取课程信息
    course = Course.query.filter_by(course_id=id).first()
    # 渲染模板
    return render_template('detail.html', course=course)

@app.route('/course_data/<int:id>/type/<type>')
def course_data(id, type):
    """
    获取课程的Json数据
    :param id: 课程id
    :param id: 课程类型
    :return: 返回课程的Json数据
    """
    data = {}  # 初始化返回值
    if type == 'week':
        # 获取最近一周
        data['title'] = '最近一周销量'
        condition = 'DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(create_time)'
        sql = f'select create_time,learner_count from sale where course_id = {id} and {condition}'
        sale_data = db.session.execute(sql)

    create_time = []  # 初始化数据
    learner_count = []  # 初始化数据
    for item in sale_data:
        # 最近一周和最近一个月的日期是date_time类型，需要转化为字符串
        # 年度每月销量日期是本身就是字符串类型，不需要转化
        create_time.append(item[0].strftime('%m-%d'))
        learner_count.append(item[1])
    data['categories'] = create_time
    data['data'] = learner_count
    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)
