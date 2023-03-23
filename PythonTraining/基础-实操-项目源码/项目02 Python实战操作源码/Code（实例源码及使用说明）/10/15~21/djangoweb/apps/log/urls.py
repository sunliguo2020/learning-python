from django.urls import path

from apps.log.views import CreateLog


urlpatterns = [
    path('create/', CreateLog.as_view(), name='create'),  # 日志配置
]
