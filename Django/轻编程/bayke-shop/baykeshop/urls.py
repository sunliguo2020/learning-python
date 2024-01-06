from django.urls import path, include

urlpatterns = [
    path('article/', include('baykeshop.apps.article.urls'))
]
