from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('getdata/', views.get_data),
    path('addata/', views.add_data),
    path('demo/', views.DemoView.as_view()),
]
