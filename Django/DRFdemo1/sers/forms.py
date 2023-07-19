# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-19 18:30
"""
from django import forms

from .models import Book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
