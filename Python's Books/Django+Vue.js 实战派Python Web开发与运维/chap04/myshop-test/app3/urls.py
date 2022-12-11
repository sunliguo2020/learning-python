# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/10 23:15
"""
from django.urls import path

from . import views

urlpatterns = [
    path('var/',views.var),
    path('for_label/',views.for_label),
    path('welcome/',views.welcome)
]