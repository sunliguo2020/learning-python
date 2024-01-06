from django.db import models

from common.db import BaseModel


# Create your models here.
class Order(BaseModel):
    """订单表"""
    ORDER_STATUS = (
        (1, "待支付"),
        (2, "待发货"),
        (3, "配送中"),
        (4, "待评价"),
        (5, "已完成"),
        (6, "已关闭"),
    )

    PAY_TYPES = (
        (1, "支付宝"),
        (2, "微信支付"),
        (3, "云闪付"),
        (4, "货到付款"),
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="下单用户",
                             help_text="下单用户")
    addr = models.CharField(verbose_name='收货地址', max_length=200)
    order_code = models.CharField(verbose_name='订单编号', help_text='订单编号', max_length=50)
    amount = models.FloatField(verbose_name='订单总金额', help_text="订单总金额")
    status = models.SmallIntegerField(verbose_name='订单状态', help_text='订单状态',
                                      default=1, choices=ORDER_STATUS)
    pay_type = models.SmallIntegerField(verbose_name='支付方式', help_text='支付方式',
                                        choices=PAY_TYPES, default=1)
    pay_time = models.DateTimeField(verbose_name='支付时间', help_text='支付时间',
                                    blank=True, null=True)
    trade_no = models.CharField(verbose_name='支付单号', help_text='支付单号', blank=True,
                                max_length=50, null=True)

    def __str__(self):
        return self.order_code

    class Meta:
        db_table = 'order'
        verbose_name = '订单表'
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    """订单商品表"""
    order = models.ForeignKey('Order', verbose_name='所属订单', help_text="所属订单",
                              on_delete=models.CASCADE)
    goods = models.ForeignKey('goods.Goods', verbose_name="商品ID", help_text='商品ID',
                              on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='商品价格', help_text='商品价格')

    number = models.IntegerField(verbose_name='商品数量', help_text='商品数量', default=1)

    class Meta:
        db_table = 'orderGoods'
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name


class Comment(BaseModel):
    """订单评论表"""
    RATES = (
        (1, '好评'),
        (2, '好评'),
        (1, '好评'),
    )
    STARS = (
        (1, '一星'),
        (2, '二星'),
        (3, '三星'),
        (4, '四星'),
        (5, '五星'),
    )

    user = models.ForeignKey('users.User', verbose_name='评论用户', help_text='评论用户',
                             on_delete=models.CASCADE)
    order = models.ForeignKey('Order', verbose_name='所属订单', on_delete=models.CASCADE)
    goods = models.ForeignKey('goods.Goods', verbose_name='所属商品', help_text='所属商品', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='评论内容', default='', max_length=150)
    rate = models.SmallIntegerField(verbose_name='评论等级', help_text='评论等级', default=1, choices=RATES, blank=True)
    star = models.SmallIntegerField(verbose_name='评论星级', default=5, choices=STARS, blank=True)

    class Meta:
        db_table = 'comment'
        verbose_name = '订单评论'
        verbose_name_plural = verbose_name
