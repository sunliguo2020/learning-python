"""djangoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', include(('apps.log.urls', 'apps.log'), namespace='log')),  # 日志配置
    path('mail/', include(('apps.mail.urls', 'apps.mail'), namespace='mail')),  # 邮件验证模块
    path('chat/', include(('apps.chat.urls', 'apps.chat'), namespace='chat')),  # 实时聊天模块
    path('message/', include(('apps.message.urls', 'apps.message'), namespace='message')),  # 消息提示模块
    path('page/', include(('apps.page.urls', 'apps.page'), namespace='page')),  # 数据分页模块
    path('ajax/', include(('apps.ajax.urls', 'apps.ajax'), namespace='ajax')),  # Ajax模块
    path('search/', include(('apps.search.urls', 'apps.search'), namespace='search')),  # 全局搜索模块
    path('', views.index),  # 首页

]
