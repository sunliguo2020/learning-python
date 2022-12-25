# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-23 14:16
"""
from django.urls import path,include
from . import views

urlpatterns = [
    path('user_reg/',views.user_reg),
               ]