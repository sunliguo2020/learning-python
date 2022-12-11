# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/11 9:43
"""

from django.urls import path, re_path
from . import views
from django.views.static import serve
from django.conf import settings

print("settings.MEDIA_ROOT",settings.MEDIA_ROOT)
urlpatterns = [
    path('upload_file/', views.upload_file),
    path('userinfoform/', views.userinfo_form),
    path('userinfomsgform/', views.userinfo_msg_form),
    path('userimg/', views.imgfileform),
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT})

]
