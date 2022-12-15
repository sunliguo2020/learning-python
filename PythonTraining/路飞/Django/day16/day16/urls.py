"""day16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin as djadmin
from django.urls import path, re_path
from django.conf import settings
from app01.views import depart, pretty, shoujihao, user, admin
from app01.views import account, task, webcam, order, chart
from django.views.static import serve

urlpatterns = [
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    path('djadmin/', djadmin.site.urls),
    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/add/', user.user_model_add),
    path('user/<int:nid>/delete/', user.user_delete),
    path('user/<int:nid>/edit/', user.user_edit),

    # 靓号管理
    path('prettynum/list/', pretty.prettynum_list),
    path('prettynum/add/', pretty.prettynum_add),
    path('prettynum/<int:nid>/edit/', pretty.prettynum_edit),
    path('prettynum/<int:nid>/delete/', pretty.prettynum_delete),

    # 手机号管理
    path('shoujihao/list/', shoujihao.shoujihao_list),
    path('shoujihao/<int:nid>/edit/', shoujihao.shoujihao_edit),
    path('shoujihao/<int:nid>/delete/', shoujihao.shoujihao_delete),
    path('shoujihao/<int:nid>/hide/', shoujihao.shoujihao_active),
    path('shoujihao/test/', shoujihao.shoujihao_test),

    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),

    # 任务管理
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),

    # 监控截图管理
    path('webcam/list/', webcam.webcam_list),
    path('webcam/upload/', webcam.upload),
    path('webcam/<int:nid>/delete/', webcam.webcam_delete),

    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/edit/', chart.chart_edit),

]
