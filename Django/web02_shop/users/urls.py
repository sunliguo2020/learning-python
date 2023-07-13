from django.urls import path

from users.views import LoginView, RegisterView2

urlpatterns = [
    # 登录
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView2.as_view(), name='login'),
    # token刷新
    # path('token/refresh',TokenRefreshView.as_view(),name = 'token_refresh'),
    # # token 校验
    # path('token/verify',TokenVerifyView.as_view(),name='token_verify'),

]
