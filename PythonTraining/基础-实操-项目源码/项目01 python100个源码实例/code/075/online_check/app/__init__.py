from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
# 基本配置
app.config["SECRET_KEY"] = "mrsoft"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:root@localhost/online_check'
        )
# 实例化SQLAlchemy类
db = SQLAlchemy(app)

# 实例化LoginManager类
login_manager = LoginManager(app)
# 跳转的页面
login_manager.login_view = 'login'
# 提示信息
login_manager.login_message = "请先登录"
# 提示样式
login_manager.login_message_category = 'danger'



