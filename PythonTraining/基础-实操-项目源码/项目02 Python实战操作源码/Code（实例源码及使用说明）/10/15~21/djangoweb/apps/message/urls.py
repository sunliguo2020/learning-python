from django.urls import path

from . import views
from apps.message.views import TipView

urlpatterns = [
    path('tip/', TipView.as_view(), name='tip'),  # 消息提示
    path('receive/', views.receive_message, name='receive'),  # 接收消息
]
