from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users import views
from users.views import LoginView, RegisterView2, UserView

urlpatterns = [
    # 登录
    # path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    # 注册
    path('register/', RegisterView2.as_view(), name='login'),
    # token刷新
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # # token 校验
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # 获取单个用户信息的路由
    path('users/<int:pk>/', UserView.as_view({'get': 'retrieve'})),
    # 上传用户头像接口
    path('<int:pk>/avatar/upload/', UserView.as_view({'post': 'upload_avatar'})),

    # 添加地址和获取地址列表
    path('address/', views.AddrView.as_view({
        "post": "create",
        "get": 'list'
    })),

    # 修改和删除收货地址
    path('address/<int:pk>/', views.AddrView.as_view({
        "delete": "destroy",
        "put": 'update'
    })),
]
