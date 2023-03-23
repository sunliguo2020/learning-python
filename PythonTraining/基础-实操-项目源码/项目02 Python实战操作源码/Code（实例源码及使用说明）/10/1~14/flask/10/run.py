from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import and_
import pymysql

app = Flask(__name__) # 实例化Flask对象
# 基本配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:root@localhost/flask_demo'
        )
db = SQLAlchemy(app)   # 实例化SQLAlchemy
class Hotel(db.Model):
    ''' Hotel表模型'''
    __tablename__ = 'hotel'  # 表名
    id = db.Column(db.Integer,primary_key=True) # 主键ID
    name = db.Column(db.String(64)) # 名称
    level = db.Column(db.Integer) # 等级
    brand = db.Column(db.String(64)) # 品牌
    features = db.Column(db.String(64)) # 特色
    score = db.Column(db.Float) # 评分
    price = db.Column(db.Float) # 最低价
    decorate_time = db.Column(db.Date) # 装修日期

@app.route('/hotel')
def index():
    # 获取所有品牌并去重
    brand_list = db.session.query(Hotel.brand).distinct()
    # 获取所有酒店特色并去重
    features_list = db.session.query(Hotel.features).distinct()
    condition = (Hotel.id > 0)
    # 根据条件筛选酒店信息
    if request.args.get('level'):  # 等级
        level = request.args.get('level')
        condition = and_(condition,Hotel.level==level)
    if request.args.get("brand"): # 品牌
        brand = request.args.get('brand')
        condition = and_(condition, Hotel.brand==brand)
    if request.args.get("features"): # 特色
        features = request.args.get("features")
        condition = and_(condition, Hotel.features==features)
    # 排序方式
    if request.args.get("tag"):
        order_string = request.args.get("tag") + ' desc'
    else :
        order_string = 'id desc'
    hotel = Hotel.query.filter(condition).order_by(order_string) # 执行查询
    return render_template('hotel.html',hotel=hotel,brand_list=brand_list,features_list=features_list)

if __name__ == "__main__":
    app.run(debug=True) # 启动项目
