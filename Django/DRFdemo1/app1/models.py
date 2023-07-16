from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')
    pwd = models.CharField(max_length=18, verbose_name='密码')
    email = models.EmailField(max_length=40, verbose_name='邮箱')
    age = models.IntegerField(verbose_name='年龄', default=18)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "userinfo"
        verbose_name = '用户信息'

