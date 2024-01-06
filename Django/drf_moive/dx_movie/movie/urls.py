from django.contrib import admin
from django.urls import path,include

from . import views

app_name = 'movie'

urlpatterns = [
    path('',views.movie_list,name='list')
]
