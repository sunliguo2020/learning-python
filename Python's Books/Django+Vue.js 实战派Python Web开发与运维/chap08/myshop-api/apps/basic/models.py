from datetime import datetime

from django.db import models

# Create your models here.
from apps.users.models import MyUser


class Address(models.Model):
    """
    用户配送地址
    """
    province = models.CharField(max_length=50, default="", verbose_name="省份")
    city = models.CharField(max_length=50, default="", verbose_name="城市")
    district = models.CharField(max_length=50, default="", verbose_name="区域")
    address = models.CharField(max_length=100, default="", verbose_name="详细地址")
    contact_name = models.CharField(max_length=20, default="", verbose_name="联系人")
    contact_mobile = models.CharField(max_length=11, default="", verbose_name="联系电话")
    user = models.ForeignKey(MyUser, verbose_name="用户" ,on_delete=models.DO_NOTHING)
    is_default=models.IntegerField(default=0,verbose_name="是否默认配送地址")
    create_date = models.DateTimeField(default=datetime.now, verbose_name="创建时间")        

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        db_table = 'd_address'
        verbose_name = "用户配送地址"
        verbose_name_plural = verbose_name