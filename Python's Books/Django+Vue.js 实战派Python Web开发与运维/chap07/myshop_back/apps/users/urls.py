# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-23 14:16
"""

from . import views
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings
from apps.users import views
urlpatterns = [
    path('user_reg/', views.user_reg),
    path('user_login/', views.user_login),
    path('ajax_login_data/', views.ajax_login_data),
    path('index/', views.index),
    path('del/<int:id>/', views.delete),
]
