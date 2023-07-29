from django.urls import path

from goods import views

urlpatterns = [
    # 商品首页获取
    path('index/', views.Index.as_view()),
    # 商品列表接口
    path('goods/', views.GoodsView.as_view({
        "get": "list",

    })),
    # 获取单个商品的接口
    path('goods/<int:pk>/', views.GoodsView.as_view({
        "get": "retrieve",

    })),

    # 收藏商品和获取收藏列表
    path("goods/collect/", views.CollectViewSet.as_view({
        "post": "create",
        "get": "list"
    })),

    # 取消收藏商品
    path("goods/collect/<int:pk>/", views.CollectViewSet.as_view({
        "delete": "destroy",

    }))

]
