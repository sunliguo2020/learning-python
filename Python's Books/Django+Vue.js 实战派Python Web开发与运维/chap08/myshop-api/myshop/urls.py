from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPICodec

schema_view = get_schema_view(title='我的商城接口文档', renderer_classes=
[SwaggerUIRenderer, OpenAPICodec])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.basic.urls')),
    path('', include('apps.goods.urls')),
    path('', include('apps.order.urls')),
    path('', include('apps.users.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('login/', obtain_jwt_token),
    path('docs/', include_docs_urls(title="我的商城")),
    path('docs2/', schema_view, name='docs'),
    path('', include('django_prometheus.urls')),
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    re_path('static/(?P<path>.*)', serve, {"document_root": settings.STATIC_ROOT}),
]
