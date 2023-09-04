# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-01 7:24
"""
from django.urls import path

from order import views

urlpatterns = [
    path('submit/', views.OrderView.as_view(
        {'post': 'create'}
    ))
]
