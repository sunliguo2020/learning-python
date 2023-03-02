# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-23 9:25
"""
import re

from django.core.exceptions import ValidationError
from django import forms


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
                                       "class": 'password',
                                   }, render_value=True
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

    # 全局钩子函数
    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        if password != re_password:
            self.add_error('re_password', ValidationError('两次密码输入不一样'))
