from django.contrib import admin
from django.urls import path,include,re_path
from apps.users import views
from django.views.static import serve
from myshop import settings
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

user_list=views.MyUserViewSet.as_view({
    'get': 'retrieve',
    'post':'create',
})

user_detail=views.MyUserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete':'destroy',
})
router=DefaultRouter()
router.register('users',views.MyUserViewSet)
urlpatterns = [
    path('users/',user_list),
    #path('app8/goods5/',user_list), # 获取或创建
    path('users/<pk>/',user_detail), # 查找、更新、删除

    path('test/',views.myuser_reg),
    path("", include(router.urls))
]
#router.register('users', views.MyUserViewSet, basename="users")