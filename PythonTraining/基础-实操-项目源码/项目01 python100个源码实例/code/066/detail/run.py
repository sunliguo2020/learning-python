from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import datetime
from sqlalchemy import desc


app = Flask(__name__)
# 基本配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:root@localhost/flask'
        )

db = SQLAlchemy(app) # 实例化SQLAlchemy类

# 创建数据表类
class Course(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
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

if __name__ == "__main__":
    app.run(debug=True)
