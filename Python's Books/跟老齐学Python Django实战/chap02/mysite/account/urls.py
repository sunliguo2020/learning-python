# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-15 22:12
"""
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
    # path('login/', views.user_login, name="user_login") # 自定义的登录
    path('login/', auth_views.LoginView.as_view(), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(), name="user_logout"),
    path('reg/', views.register, name="user_reg"),

]
