from django.urls import path, re_path

from apps.mail.views import VerifyMail, UserActivate


urlpatterns = [
    path('verify/', VerifyMail.as_view(), name='verify'),  # 邮件验证
    re_path(r'^activate/(?P<token>.*)$', UserActivate.as_view(), name='activate'),  # 用户激活
]
