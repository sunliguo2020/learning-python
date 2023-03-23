from app import db,login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(125), nullable=False)
    email = db.Column(db.String(125), nullable=False)
    password = db.Column(db.String(125), nullable=False)
    is_admin = db.Column(db.Boolean, default=0)
    department = db.Column(db.String(125), nullable=False)
    position = db.Column(db.String(125), nullable=False)
    hiredate = db.Column(db.Date,nullable=False)
    status = db.Column(db.Boolean, default=0)
    log = db.relationship("Log", backref="user")

class Log(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    update_content = db.Column(db.Text)
    update_time = db.Column(db.DateTime,default=datetime.now)

