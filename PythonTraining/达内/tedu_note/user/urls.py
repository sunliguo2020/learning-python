# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-03 16:59
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('reg/', views.reg_view),
    path('login/', views.login_view),
]
