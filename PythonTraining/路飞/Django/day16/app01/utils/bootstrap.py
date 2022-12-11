# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 12:23
"""
from django import forms


class BootStrap:
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # 循环ModelForm中所有的字段，给每一个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # 字段中有属性，保留原来的属性。没有属性，才设置
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootStrapForm(BootStrap, forms.Form):
    pass
