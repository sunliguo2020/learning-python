# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-07 17:32
"""
from django.urls import path,include
from apps.basic import views
app_name = 'basic'
urlpatterns = [
    path('index/',views.index,name='basic_index'),
]
