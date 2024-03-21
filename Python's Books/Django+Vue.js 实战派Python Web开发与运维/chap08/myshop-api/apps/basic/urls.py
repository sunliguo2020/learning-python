from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from apps.basic import views

router=DefaultRouter()
router.register('address',views.AddressViewset,basename="address")

urlpatterns = [
    path("",include(router.urls))
]