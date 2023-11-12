# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-23 14:16
"""

from django.urls import path

from apps.users import views

app_name = 'users'
urlpatterns = [
    path('user_reg/', views.user_reg),
    path('user_login/', views.user_login),
    path('ajax_login_data/', views.ajax_login_data),
    path('index/', views.index, name='users_index'),
    path('del/<int:id>/', views.delete),
    path('edit/<id>/', views.edit, name='users_edit'),
]
