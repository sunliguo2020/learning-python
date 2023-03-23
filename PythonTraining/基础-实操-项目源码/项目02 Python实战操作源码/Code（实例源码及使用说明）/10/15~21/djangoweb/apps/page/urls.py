from django.urls import re_path

from apps.page.views import IndexView

urlpatterns = [
    re_path(r'^index(?P<page>\d+)$', IndexView.as_view(), name='index'),  # 数据分页
]
