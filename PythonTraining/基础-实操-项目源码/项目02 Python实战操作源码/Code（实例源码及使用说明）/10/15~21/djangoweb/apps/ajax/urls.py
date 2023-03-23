from django.urls import path

from . import views

urlpatterns = [
    path('init/', views.init, name='init'),  # 初始加载一级菜单
    path('type_detail', views.find_type, name='type_detail'),  # 具体类型
]
