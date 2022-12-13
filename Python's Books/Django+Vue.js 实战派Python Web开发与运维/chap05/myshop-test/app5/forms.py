# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/11 9:56
"""
from django import forms
from django.core.exceptions import ValidationError
import re
from . import models


def mobile_validate(value):
    mobile_re = re.compile(r'(13[0-9]|15[0123456789]|17[678]|18[0-9]|14[57]|)[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


def age_validate(value):
    if value < 1 | value > 120:
        raise ValidationError('年龄范围为1-120岁')


class UserInfoForm(forms.Form):
    """用户状态"""
    STATUS = (
        (None, '请选择'),
        (1, '正常'),
        (2, '无效'),
    )
    username = forms.CharField(label='用户名称', min_length=6,
                               widget=forms.widgets.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': '请输入用户名称'
                                   }
                               ))
    password = forms.CharField(label='密码', min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(
                                   attrs={
                                       "class": 'password',
                                   }, render_value=True
                               ))
    age = forms.IntegerField(label='年龄', initial=1)
    mobile = forms.CharField(label='手机号码')
    status = forms.ChoiceField(label='用户状态', choices=STATUS)
    createdate = forms.DateTimeField(label='创建时间', required=False,
                                     )


class UserInfo_Msg_form(forms.Form):
    """用户状态"""
    STATUS = (
        (None, '请选择'),
        (1, '正常'),
        (2, '无效'),
    )
    username = forms.CharField(label='用户名称', min_length=6,
                               widget=forms.widgets.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': '请输入用户名称'
                                   }
                               ),
                               error_messages={
                                   'required': '用户姓名不能为空',
                                   'min_length': '长度最少为6位',
                                   'invalid': '不能有特殊字符'
                               })
    password = forms.CharField(label='密码', min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(
                                   attrs={
                                       "class": 'password',
                                   }, render_value=True
                               ),
                               error_messages={
                                   'max_length': "密码最长10位",
                                   'required': '密码不能为空',
                                   'min_length': '密码最少6位'
                               })
    age = forms.IntegerField(label='年龄', initial=1,
                             validators=[age_validate],
                             error_messages={
                                 'required': '年龄不能为空'
                             })
    mobile = forms.CharField(label='手机号码',
                             validators=[mobile_validate],
                             error_messages={
                                 'required': '手机号不能为空'
                             })
    status = forms.ChoiceField(label='用户状态', choices=STATUS,
                               error_messages={
                                   "required": '用户状态不能为空'
                               })
    createdate = forms.DateTimeField(label='创建时间', required=False)


class ImgFileForm(forms.Form):
    name = forms.CharField()
    headimg = forms.FileField(label='头像')


class UserBaseInfoModelForm(forms.ModelForm):
    class Meta:

        # 定义关联模型
        model = models.UserBaseInfo
        # 定义需要在表单中展示的字段

        fields = ['username',
                  'password',
                  'age',
                  'mobile',
                  'status',
                  ]
        # 如果要显示全部字段
        # fields = '__all__'

        # 如果在Models中定义了名称，则在这里不再定义
        labels = {
            'age': '年龄',
            'mobile': '手机信息',
        }
        # 将文本框渲染为密码输入框
        widgets = {
            "password": forms.widgets.PasswordInput(attrs={
                "class": "password",

            }, render_value=True)
        }

        error_message = {
            "username": {'required': '用户姓名不能为空',
                         'min_length': '长度最少6位',
                         'invalid': '输入正确的姓名'},
            'password': {
                'max_length': '密码最长为10位',
                'required': '密码不能为空',
                'min_length': '密码最少6位'
            },
            "age": {
                'required': '年龄不能为空',
            },
            'mobile': {
                'required': '手机号码不能为空',
            },
            'status': {
                'required': '用户状态不能为空',
            }
        }
