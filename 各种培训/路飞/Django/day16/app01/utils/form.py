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


class MobileEditModelForm(BootStrapModelForm):
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
