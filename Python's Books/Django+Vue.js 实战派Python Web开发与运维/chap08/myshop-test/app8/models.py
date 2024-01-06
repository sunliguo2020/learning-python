from datetime import datetime

from app6.models import MyUser
from django.db import models


# Create your models here.


class GoodsCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='分类名称', default='')
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父类", on_delete=models.DO_NOTHING,
                               related_name="sub_cat")
    logo = models.ImageField(default='', verbose_name="分类logo图片", upload_to="uploads/goods_img/")
    is_nav = models.BooleanField(default=False, verbose_name='是否显示在导航栏')
    sort = models.IntegerField(verbose_name='排序')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '商品分类'
        # db_table='d_goods_category8'


class Goods(models.Model):
    STATUS = (
        (0, '正常'),
        (1, '下架'),
    )
    name = models.CharField(max_length=50, verbose_name='商品名称', default='')
    category = models.ForeignKey(GoodsCategory, blank=True, null=True, verbose_name='商品分类',
                                 on_delete=models.DO_NOTHING)
    market_price = models.DecimalField(max_digits=8, default=0, decimal_places=2, verbose_name='市场价格')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='实际价格')
    unit = models.CharField(max_length=10, verbose_name='计量单位', blank=True, null=True)
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    amount = models.IntegerField(default=0, verbose_name="销售量")
    stock_num = models.IntegerField(default=0, verbose_name="库存数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    status = models.IntegerField(default=0, choices=STATUS)
    main_img = models.ImageField(verbose_name='商品主图', blank=True, null=True, upload_to='goods/images/')
    is_recommend = models.BooleanField(default=False, verbose_name="是否推荐")
    user = models.ForeignKey(MyUser, blank=True, null=True, verbose_name="用户", on_delete=models.DO_NOTHING)
    createDate = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品表'
        # db_table = 'd_goods8'
