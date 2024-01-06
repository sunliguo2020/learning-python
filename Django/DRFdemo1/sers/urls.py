from django.urls import path, re_path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('book/', views.BookView.as_view()),
    path('book2/', views.BookGenericApiView.as_view()),
    re_path('book/(\d+)', views.BookDetailView.as_view()),
]
