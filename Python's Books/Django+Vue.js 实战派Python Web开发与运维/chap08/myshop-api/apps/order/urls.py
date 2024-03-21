from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from apps.order import views

router=DefaultRouter()
router.register('cart',views.CartViewset,basename="cart")

urlpatterns = [
    #GenericViewSet
    path('order/',views.OrderView.as_view()),#get，Post
    #router.register('indexgoods',views.IndexCategoryViewset,basename="indexgoods"),
    path("",include(router.urls))
]