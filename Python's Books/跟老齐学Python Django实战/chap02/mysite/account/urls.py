# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-15 22:12
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    # path('login/', views.user_login, name="user_login") # 自定义的登录
    path('login/', auth_views.LoginView.as_view(), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(), kwargs={"template_name": "account/logout.html"},
         name="user_logout", ),
    path('reg/', views.register, name="user_reg"),
    path('password-change/', auth_views.PasswordChangeView.as_view(),
         {'post_change_done': "/account/password-change-done"}, name="password_change"),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('my-information/', views.myself, name="my_information"),
    path('edit-my-information/', views.myself_edit, name="edit_my_information"),
    path('my-image/', views.my_image, name="my_image"),

]
