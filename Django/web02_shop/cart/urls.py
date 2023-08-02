from django.urls import path

from cart import views

urlpatterns = [
    # 添加商品到购物车和获取购物车商品列表
    path('goods/', views.CartView.as_view({'get': 'list',
                                           'post': 'create'})),
    # 修改购物车商品的数量
    path('goods/<int:pk>/', views.CartView.as_view({
        "put": 'update_goods_number',
        "delete": "destroy"
    })),
    # 修改商品的选中状态
    path('goods/<int:pk>/checked/', views.CartView.as_view({
        "put": "update_goods_status"
    })),

]
