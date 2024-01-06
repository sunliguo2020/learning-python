from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('def_index/', views.index,name='index'),
    path('cls_index/', views.IndexView.as_view(),name='index2'),
    path('listview/', views.BaykeArticleListView.as_view(),name='listview'),
    path('detailview/<int:pk>/', views.BaykeArticleDetailView.as_view(),name='detailview'),
]
