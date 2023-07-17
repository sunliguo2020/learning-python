from ckeditor.fields import RichTextField
from django.db import models

from common.db import BaseModel


# Create your models here.


class GoodsGroup(BaseModel):
    """商品分类"""
    name = models.CharField(max_length=20, verbose_name="名称")
    image = models.ImageField(verbose_name="分类图标")
    status = models.BooleanField(default=False, verbose_name="是否启用")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'goods_group'
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name


class Goods(BaseModel):
    """商品模型类"""
    group = models.ForeignKey('GoodsGroup', verbose_name='分类', help_text='分类', max_length=20,
                              on_delete=models.CASCADE)
    title = models.CharField(verbose_name='标题', help_text='标题', max_length=200, default='')
    desc = models.CharField(verbose_name="商品描述", help_text="商品描述", max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品价格", help_text="商品价格")
    cover = models.ImageField(verbose_name='封面图连接', help_text="封面链接", default='', null=True)
    stock = models.IntegerField(verbose_name='库存', default=1, help_text='库存', blank=True)
    sales = models.IntegerField(default=0, help_text="销量", verbose_name="销量", blank=True)
    is_on = models.BooleanField(default=False, verbose_name='是否上架', help_text='是否上架', blank=True)
    recommend = models.BooleanField(default=False, verbose_name="是否推荐", help_text="是否推荐", blank=True)

    class Meta:
        db_table = 'goods'
        verbose_name = '商品表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Detail(BaseModel):
    """商品详情"""
    goods = models.OneToOneField('Goods', verbose_name='商品', on_delete=models.CASCADE)
    producer = models.CharField(verbose_name='厂商', help_text='厂商', max_length=200)
    norms = models.CharField(verbose_name='规格', help_text='规格', max_length=200)
    # pip install django-ckeditor
    detail = RichTextField(blank=True, verbose_name='商品详情')

    class Meta:
        db_table = 'detail'
        verbose_name = '商品详情表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods


class GoodsBanner(BaseModel):
    """商品轮播图
    """
    title = models.CharField(verbose_name='轮播图名称', help_text='轮播图名称', max_length=20, default='')
    image = models.ImageField(verbose_name='轮播图链接', help_text='轮播图链接', blank=True, null=True)
    status = models.BooleanField(verbose_name='是否启用', help_text='是否启用', default=False, blank=True)
    seq = models.BooleanField(verbose_name='顺序', help_text='顺序', default=1, blank=True)

    class Meta:
        db_table = 'banner'
        verbose_name = '首页商品轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Collect(BaseModel):
    """收藏商品"""
    user = models.ForeignKey('users.User', help_text='用户ID', verbose_name='用户ID', on_delete=models.CASCADE,
                             blank=True)
    goods = models.ForeignKey('Goods', help_text="商品ID", verbose_name='商品ID', on_delete=models.CASCADE)

    class Meta:
        db_table = 'collect'
        verbose_name = '收藏商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods
