from django.urls import path
from . import views

app_name = 'blog'   # 定义一个命名空间，用来区分不同应用之间的链接地址

urlpatterns = [ 
    path('', views.index, name='index'),
]