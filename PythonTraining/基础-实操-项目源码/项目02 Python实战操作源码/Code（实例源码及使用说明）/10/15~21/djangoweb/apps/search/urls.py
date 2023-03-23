from django.urls import path
from . import views

urlpatterns = [
    # 搜索引擎
    path('find/', views.MySearchView(), name='haystack'),
]
