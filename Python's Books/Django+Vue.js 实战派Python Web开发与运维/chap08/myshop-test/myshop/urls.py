"""myshop URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
# from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app8/', include('app8.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('api-jwt-token-auth/', obtain_jwt_token, name='api_jwt_token_auth'),
    path('docs/', include_docs_urls(title='我的商城接口文档'))
]
