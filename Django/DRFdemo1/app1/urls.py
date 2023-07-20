from django.urls import path, re_path

from . import views

urlpatterns = [
    path('users/', views.user_list),
    re_path(r'users/(.+?)/', views.user_detail),
    path('book/', views.BookView.as_view()),
    path('book2/', views.BookView2.as_view()),
]
