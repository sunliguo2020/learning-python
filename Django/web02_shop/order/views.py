import time

from django.db import transaction
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from cart.models import Cart
from users.models import Addr
from .models import Order, OrderGoods
from .permissions import OrderPermission
from .serializers import OrderSerializer


# Create your views here.
class OrderView(GenericViewSet):
    """订单详情和订单列表"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, OrderPermission]

    @transaction.atomic
    def create(self, request, *arg, **kwargs):
        """提交订单视图，需要开启事务"""
        # 设置事务保存点
        save_id = transaction.savepoint()
        # 获取请求参数
        addr = request.data.get('addr')
        if not Addr.objects.filter(user=request.user, id=addr).exists():
            return Response({"error": "传入的收货地有误！"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        addr_obj = Addr.objects.get(id=addr)
        addr_str = f"{addr_obj.province}{addr_obj.city}{addr_obj.county}{addr_obj.address}" \
                   f"{addr_obj.name}{addr_obj.phone}"
        try:
            # 获取购物车中所有选中的商品
            cart_goods = Cart.objects.filter(user=request.user, is_checked=True)
            if not cart_goods.exists():
                return Response({"error": "订单提交失败,没有选中的商品"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            # 生成一个订单编号
            order_code = str(int(time.time())) + str(request.user.id)

            # 创建订单
            order = Order.objects.create(user=request.user, addr=addr_str, order_code=order_code, amount=0)
            amount = 0
            # 遍历购物车中选中的所有商品
            for cart in cart_goods:
                # 获取商品的数量
                num = cart.number
                # 获取商品的价格
                price = cart.goods.price
                # 将价格进行累加
                amount += price * num

                # 判断商品购买数量是否大于商品库存
                if num > cart.goods.stock:
                    # 库存不足（事务回滚）
                    transaction.savepoint_rollback(save_id)
                    return Response({"error": f"订单创建失败,购买商品{cart.goods.title}的数量大于库存"},
                                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                else:
                    # 商品的库存减去销售量
                    cart.goods.stock -= num
                    # 增加销量
                    cart.goods.sales += num
                    cart.goods.save()

                # 在订单商品表中新增一条数据
                OrderGoods.objects.create(order=order, goods=cart.goods,
                                          price=price,
                                          number=num)
                # 购物车中删除该商品
                cart.delete()

            # 修改订单金额
            order.amount = amount
            # 保存订单
            order.save()
        except:
            # 事件回滚
            transaction.savepoint_rollback(save_id)
            return Response({"status_code": 400, "message": "订单创建失败", "data": None},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            # 提交事件
            transaction.savepoint_commit(save_id)
            # 提交订单信息
            orders = OrderSerializer(instance=order)

            return Response({"status_code": 201, "message": "订单创建成功", "data": orders.data},
                            status=status.HTTP_201_CREATED)
