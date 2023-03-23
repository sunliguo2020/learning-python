from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_script import Manager,Shell

app = Flask(__name__) # 实例化Flask对象
# 基本配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:root@localhost/flask_demo'
        )

db = SQLAlchemy(app)   # 实例化SQLAlchemy
manager = Manager(app) # 实例化Manager类

def make_shell_context():
    '''回调函数'''
    return dict(app=app,db=db,Student=Student,Class=Class)

manager.add_command("shell",Shell(make_context=make_shell_context)) # 添加Shell命令

# 学生和课程关系
student_identifier = db.Table('student_identifier',
    db.Column('class_id', db.Integer, db.ForeignKey('classes.id')), # 关联外键
    db.Column('user_id', db.Integer, db.ForeignKey('students.id'))   # 关联外键
)

# 学生数据模型
class Student(db.Model):
    __tablename__ = 'students' # 表名
    id = db.Column(db.Integer, primary_key=True) # 学生ID
    name = db.Column(db.String(64)) # 学生名称
    email = db.Column(db.String(128), unique=True) # 学生邮箱
    classes = db.relationship("Class",secondary=student_identifier) # 映射关系


# 课程数据模型
class Class(db.Model):
    __tablename__ = 'classes' # 表名
    id = db.Column(db.Integer, primary_key=True) # 班级ID
    name = db.Column(db.String(128), unique=True) # 班级名称
    students = db.relationship("Student",secondary=student_identifier) # 映射关系

if __name__ == "__main__":
    manager.run() # 启动项目
