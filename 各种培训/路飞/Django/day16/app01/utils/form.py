# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 12:53
"""
from django.core.exceptions import ValidationError
from app01.utils.bootstrap import BootStrapModelForm
from django import forms
from app01 import models
from app01.utils.encrypt import md5
from app01.utils.bootstrap import BootStrapForm


class MobileEditModelForm(BootStrapModelForm):
    """靓号编辑"""

    # mobile = forms.CharField(disabled=True, label='手机号')
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def clean_mobile(self):
        # 当前编辑的哪一行的id
        # self.instance.pk
        txt_mobible = self.cleaned_data['mobile']

        if len(txt_mobible) != 11:
            # 验证不通过
            raise ValidationError("格式错误")
        # 检查手机号是否已经存在
        if models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobible).exists():
            raise ValidationError("手机号已经存在")
        return txt_mobible


class MobileModelForm(BootStrapModelForm):
    # 校验方式1
    # mobile = forms.CharField(
    #     label='手机号',
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    # )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # fields = __all__
        # exclude = []

    # 验证方式2
    def clean_mobile(self):
        txt_mobible = self.cleaned_data['mobile']
        if len(txt_mobible) != 11:
            # 验证不通过
            raise ValidationError("格式错误")
        # 检查手机号是否已经存在
        if models.PrettyNum.objects.filter(mobile=txt_mobible).exists():
            raise ValidationError("手机号已经存在")
        return txt_mobible


class ShoujihaoModelsForm(BootStrapModelForm):
    class Meta:
        model = models.Shoujihao
        fields = ['PROD_INST_ID',
                  'CUST_ID',
                  'LATN',
                  'BUSI_NBR',
                  'USER_NAME',
                  'CUST_NAME',
                  'INSTALL_ADDR',
                  'CERTIFICATES_NBR',
                  'mod_time']


class UserModelForm(BootStrapModelForm):
    name = forms.CharField(min_length=3, label='用户名')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'dpart']


class AdminModelForm(BootStrapModelForm):
    """
    新建管理员
    """
    confirm_password = forms.CharField(max_length=32,
                                       label='确认密码',
                                       widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_username(self):
        # 检查管理员是否已经存在
        username_txt = self.cleaned_data.get('username')
        # 查询数据库中是否存在此管理员
        if models.Admin.objects.filter(username=username_txt).first():
            raise ValidationError("此管理员已经存在!")
        return username_txt

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))

        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库中就是什么
        return confirm


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']

    def clean_username(self):
        # 检查用户名是否已经存在
        username_txt = self.cleaned_data.get('username')
        # 除了此id外没有是这个名的管理员
        if models.Admin.objects.exclude(id=self.instance.pk).filter(username=username_txt).exists():
            raise ValidationError("用户名已经存在")
        return username_txt


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(max_length=32,
                                       label='确认密码',
                                       widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和输入的密码是否一致
        if models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists():
            raise ValidationError("不能和以前的密码相同")

        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))

        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库中就是什么
        return confirm


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ['username', 'password']


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets={
            "detail":forms.TextInput
        }
