from django.urls import path

from . import views

urlpatterns = [
    # path('users/', views.user_list),

    # re_path(r'users/(.+?)/', views.user_detail),
    # path('users/<int:id>/', views.user_detail),

    path('users/', views.UserView.as_view({"get": 'list', 'post': 'create'})),
    path('users/<int:id>/', views.UserView.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'DELETE': "destroy"})),

]
