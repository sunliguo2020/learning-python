# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-18 12:02
"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证URL
    path('', include('django.contrib.auth.urls')),
    # 注册页面
    path('register/', views.register, name='register')
]
