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


class Addr(models.Model):
    user = models.ForeignKey("UserInfo",verbose_name='所属用户',on_delete=models.CASCADE)
    mobile = models.CharField(verbose_name='手机号',max_length=19)
    city = models.CharField(verbose_name='城市',max_length=20)
    info = models.CharField(verbose_name="详细地址",max_length=200)

    def __str__(self):
        return self.info

