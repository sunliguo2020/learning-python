"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app6 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', views.user_reg),  # 访问路由，指定视图函数
    path('login/', views.user_login),
    path('user_reg/', views.myuser_reg),
    path('myuser_login/', views.myuser_login, name='app6_myuser_login'),
    path('myuser_logout/', views.myuser_logout, name='app6_myuser_logout'),
    path('index/',views.user_index),
    path('app6/test/',views.test)
]
