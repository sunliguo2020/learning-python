# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-19 19:43
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index')

]
