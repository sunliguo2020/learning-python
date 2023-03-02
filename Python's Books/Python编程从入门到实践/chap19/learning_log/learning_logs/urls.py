# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/7 8:31
"""
"""定义learning_logs的URL模式"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细信息
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面。
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
