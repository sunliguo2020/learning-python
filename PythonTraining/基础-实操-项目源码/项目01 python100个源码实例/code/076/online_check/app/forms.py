from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('邮箱',
                        validators=[
                            DataRequired(message="邮箱不能为空"),
                            Email()])
    password = PasswordField('密码',
                             validators=[
                                 DataRequired(message="密码不能为空"),
                                 Length(min=6, max=25, message='密码长度为6-25个字符'),
                             ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SettingForm(FlaskForm):
    password = PasswordField('原始密码',
                             validators=[
                                 DataRequired(message="原始密码不能为空"),
                                 Length(min=6, max=25, message='密码长度为6-25个字符'),
                             ])
    new_password = PasswordField('新密码',
                                 validators=[
                                     DataRequired(message="新密码不能为空"),
                                     Length(min=6, max=25, message='密码长度为6-25个字符')])
    confirm_password = PasswordField('确认密码',
                                     validators=[
                                         DataRequired(message="确认密码不能为空"),
                                         EqualTo('new_password', message="2次输入密码不一致")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class InfoForm(FlaskForm):
    username = StringField('姓名',
                            validators=[
                                DataRequired(message="姓名不能为空"),
                                Length(min=2, max=60, message='密码长度为2-25个字符'),
                            ],
                            render_kw={'class': 'form-control','readonly': True}
                           )
    department = StringField('部门',
                        validators=[
                            DataRequired(message="部门不能为空"),
                            Length(min=2, max=60, message='密码长度为2-25个字符'),
                            ],
                            render_kw={'class': 'form-control'})
    position = StringField('职务',
                        validators=[
                            DataRequired(message="职务不能为空"),
                            Length(min=2, max=60, message='密码长度为2-25个字符'),
                            ],
                        render_kw={'class': 'form-control'})
    hiredate = DateField('入职时间',
                        validators=[
                            DataRequired(message="入职日期不能为空"),
                            ],
                        render_kw={'class': 'form-control'},
                        id="hiredate",
                        format='%Y-%m-%d'
                           )
