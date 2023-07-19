from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('book/', views.BookView.as_view()),
    path('book2/', views.BookView2.as_view()),
]
