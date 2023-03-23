from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import datetime


app = Flask(__name__)
# 基本配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:root@localhost/flask'
        )

db = SQLAlchemy(app) # 实例化SQLAlchemy类

# 创建数据表类
class Course(db.Model):
    course_id = db.Column(db.BigInteger,nullable=False,primary_key=True)
    product_id = db.Column(db.BigInteger,nullable=False)
    product_type = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(125), nullable=False)
    provider = db.Column(db.String(125), nullable=False)
    score = db.Column(db.Float(2))
    score_level = db.Column(db.Integer)
    learner_count = db.Column(db.Integer)
    lesson_count = db.Column(db.Integer)
    lector_name = db.Column(db.String(125))
    original_price = db.Column(db.Float(2))
    discount_price = db.Column(db.Float(2))
    discount_rate = db.Column(db.Float(2))
    img_url = db.Column(db.String(125))
    big_img_url = db.Column(db.String(125))
    description = db.Column(db.Text)


@app.route('/')
def index():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)
