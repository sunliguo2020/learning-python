# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-10-06 9:24
"""
from django.urls import path

from .views import index
urlpatterns = [
    path('index/', index),

]
