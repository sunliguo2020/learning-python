from django.db import models
from apps.users.models import *
from apps.goods.models import *


class Cart(models.Model):
    '''
    购物车模型
    '''
    user = models.ForeignKey(MyUser, null=True, blank=True, verbose_name='用户', on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(Goods, null=True, blank=True, verbose_name='商品', on_delete=models.DO_NOTHING)
    goods_num = models.IntegerField(default=1, verbose_name='购物车中商品数量')

    def __str__(self):
        return str(self.goods.id)

    class Meta:
        managed = True
        db_table = 'd_cart'
        verbose_name = "购物车"
        #unique_together = ("user", "goods")  # 联合索引


class Order(models.Model):
    ORDER_STATUS=(
        ("paying","待支付"),
        ("payed","已支付"),
        ("shipping","配送中"),
        ("complete","订单结束"),
        ("cancel", "订单取消"),
    )
    order_sn = models.CharField(max_length=50, null=True, blank=True,verbose_name="订单号")
    order_total = models.IntegerField(default=0,verbose_name="商品总件数")
    order_price =models.DecimalField(default=0,max_digits=10, decimal_places=2,verbose_name="订单总金额")
    address = models.CharField(max_length=100, default="", verbose_name="收货地址")
    contact_name = models.CharField(max_length=20, default="", verbose_name="联系人")
    contact_mobile = models.CharField(max_length=11, default="",verbose_name="联系电话")
    pay_method = models.IntegerField(default=0, verbose_name="支付方式")
    memo = models.CharField(max_length=200,default='', verbose_name="订单备注")
    order_state = models.CharField(max_length=20,choices=ORDER_STATUS,default='paying',verbose_name="用户")
    user = models.ForeignKey(MyUser, verbose_name="用户", on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        managed = True
        db_table = 'd_order'


class OrderGoods(models.Model):
    '''
    订单商品关联表
    '''
    order = models.ForeignKey(Order, verbose_name="订单主表",  on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(Goods, verbose_name="商品表", on_delete=models.DO_NOTHING)
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")
    #保留下订单时的价格快照，因为会发生变化
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="商品价格")

    create_date = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        managed = True
        db_table = 'd_order_goods'