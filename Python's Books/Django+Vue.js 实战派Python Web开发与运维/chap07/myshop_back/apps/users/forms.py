# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-23 9:25
"""
import re

from django import forms
from django.core.exceptions import ValidationError

from .models import MyUser


# 手机验证函数
def mobile_validate(value):
    mobile_re = re.compile(r'(13[0-9]|15[0123456789]|17[678]|18[0-9]|14[57]|)[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class UserRegForm(forms.Form):
    username = forms.CharField(label='用户名', min_length=6,
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '请输入用户名'}
                               ),
                               error_messages={
                                   'required': '用户名不能为空',
                                   'min_length': '长度最少为6位',
                               })
    password = forms.CharField(label='密码', min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(
                                   attrs={
                                       # 指定样式类名
                                       "class": 'form-control',
                                   },
                                   render_value=True  # 在页面校验不通过后，页面上的值还存在
                               ),
                               error_messages={
                                   'max_length': '密码最长为10位',
                                   'required': '密码不能为空',
                                   'min_length': '密码最少为6位'
                               }
                               )
    re_password = forms.CharField(label='确认密码', min_length=6, max_length=10,
                                  widget=forms.widgets.PasswordInput(
                                      attrs={
                                          'class': 'form-control',
                                      },
                                      render_value=True
                                  ),
                                  error_messages={
                                      'max_length': '密码最长为10位',
                                      'required': '密码不能为空',
                                      'min_length': '密码最少为6位'
                                  }
                                  )

    nickname = forms.CharField(label="昵称", max_length=20, required=False,
                               widget=forms.widgets.TextInput(
                                   # 其中class样式为form-control，这是bootstrap的样式
                                   attrs={'class': 'form-control', 'placeholder': "请输入用户昵称"}),
                               error_messages={
                                   'required': '用户昵称不能为空',
                                   'max_length': '昵称长度不能超过20位',
                               })
    email = forms.EmailField(label="邮箱",
                             widget=forms.widgets.EmailInput(
                                 attrs={'class': 'form-control', }),
                             error_messages={
                                 'required': '邮箱不能为空',
                                 'invalid': '邮箱格式不对',
                             })
    mobile = forms.CharField(label="手机号码", validators=[mobile_validate],
                             widget=forms.widgets.TextInput(
                                 attrs={'class': 'form-control', }),
                             error_messages={
                                 'required': '手机号码不能为空',
                             })
    user_img = forms.ImageField(label="用户头像", required=False, widget=forms.widgets.FileInput(
        attrs={'class': 'form-control'}))

    # 全局钩子函数
    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        if password != re_password:
            self.add_error('re_password', ValidationError('两次密码输入不一样'))


class UsersForm(forms.ModelForm):
    birthday = forms.DateField(label='出生日期', widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加 class=“form-control"
        for name, field in self.fields.items():
            # if name == 'password':
            #   continue
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    class Meta:
        model = MyUser
        fields = ['username', 'truename', 'mobile', 'birthday', 'sex', 'user_img']
        # widgets = {"username": forms.TextInput(attrs={"class": "form-control",
        #                                                  'placeholder': '请输入用户名'})}
        # 如果model中定义了名称，则在这里不用再定义。
        labels = {
            'username': '用户名',
        }
        error_messages = {
            "username": {
                'required': '用户名不能为空'
            }
        }
