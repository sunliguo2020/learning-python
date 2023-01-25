# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-15 20:50
"""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.blog_title,name='blog_title'),
    path('<int:article_id>/',views.blog_article,name='blog_detail'),
]