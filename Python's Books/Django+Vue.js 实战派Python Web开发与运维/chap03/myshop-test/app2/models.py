from django.db import models
from django.urls import reverse


# Create your models here.
class UserBaseInfo(models.Model):
    id = models.AutoField(verbose_name='编号', primary_key=True)
    username = models.CharField(verbose_name='用户名称', max_length=30)
    password = models.CharField(verbose_name='密码', max_length=20)
    status = models.CharField(verbose_name='状态', max_length=1)
    createdate = models.DateTimeField(verbose_name='创建日期', db_column='createDate')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('app2_userinfo', kwargs={'id': self.pk})

    class Meta:
        verbose_name = '人员基本信息'
        db_table = 'UserBaseInfo2'
