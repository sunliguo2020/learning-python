from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(Form):
    username = StringField(
        '用户名',
        [DataRequired(),Length(min=4, max=25,message="请填写4-25位长度的用户名")],
        render_kw = {'class': 'form-control', 'placeholder': '请填写4-25位长度的用户名'}
    )
    email = StringField(
        '邮箱',
        [DataRequired(),Email(message="请填写正确格式的邮箱")],
        render_kw={'class': 'form-control', 'placeholder': '请填写邮箱'}
    )
    password = PasswordField(
        '密码',
        [DataRequired(),Length(min=6, max=20,message="请填写6-20位长度的用户名")],
        render_kw={'class': 'form-control', 'placeholder': '请填写密码'}
    )
    confirm = PasswordField(
        '确认密码',
        [DataRequired(),EqualTo('password', message='2次输入密码必须匹配')],
        render_kw={'class': 'form-control', 'placeholder': '请再次确认密码'}
    )
    accept_tos = BooleanField(
        '接收注册协议',
        [DataRequired()],
    )