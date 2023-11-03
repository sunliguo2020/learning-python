from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('def_index/', views.index,name='index'),
    path('cls_index/', views.IndexView.as_view(),name='index2'),
]
