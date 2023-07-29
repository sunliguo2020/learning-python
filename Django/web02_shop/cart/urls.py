from django.urls import path

from cart import views

urlpatterns = [
    path('goods/', views.CartView.as_view({'get': 'list', 'post': 'create'}))
]
