from apps.users.models import *
from django import forms
from django.core.exceptions import ValidationError
import re

def mobile_validate(value):
    mobile_re = re.compile(
        r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class UserRegForm(forms.Form):
    username = forms.CharField(label="用户名", min_length=6,
                               widget=forms.widgets.TextInput(
                                   #其中class样式为form-control，这是bootstrap的样式
                                   attrs={'class': 'form-control', 'placeholder': "请输入用户名"}),
                               error_messages={
                                   'required': '用户姓名不能为空',
                                   'min_length': '长度最少6位',
                               })
    password = forms.CharField(label="密码", min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(
                                   #render_value=True，页面校验不通过后，页面上该值还存在
                                   attrs={"class": "form-control"}, render_value=True),
                               error_messages={
                                   'max_length': '密码最长10位',
                                   'required': '密码不能为空',
                                   'min_length': '密码最少6位'
                               })
    re_password = forms.CharField(label="确认密码", min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(
                                   #render_value=True，页面校验不通过后，页面上该值还存在
                                   attrs={"class": "form-control"}, render_value=True),
                               error_messages={
                                   'max_length': '密码最长10位',
                                   'required': '密码不能为空',
                                   'min_length': '密码最少6位'
                               })
    nickname = forms.CharField(label="昵称", max_length=20,required=False,
                               widget=forms.widgets.TextInput(
                                   #其中class样式为form-control，这是bootstrap的样式
                                   attrs={'class': 'form-control', 'placeholder': "请输入用户昵称"}),
                               error_messages={
                                   'required': '用户昵称不能为空',
                                   'max_length': '昵称长度不能超过20位',
                               })
    email = forms.EmailField(label="邮箱",
                               widget=forms.widgets.EmailInput(
                                   attrs={'class': 'form-control',}),
                               error_messages={
                                   'required': '邮箱不能为空',
                                   'invalid': '邮箱格式不对',
                               })
    mobile = forms.CharField(label="手机号码", validators=[mobile_validate],
                                widget=forms.widgets.TextInput(
                                   attrs={'class': 'form-control',}),
                                error_messages={
                                    'required': '手机号码不能为空',
                                })
    user_img=forms.ImageField(label="用户头像",required=False, widget=forms.widgets.FileInput(
                                   attrs={'class': 'form-control'}))
    
    # 全局钩子函数
    def clean(self):
        password =  self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        print(password)
        if password != re_password:
            #raise forms.ValidationError("二次密码输入不一致")
            self.add_error("re_password",ValidationError("二次密码输入不一致"))