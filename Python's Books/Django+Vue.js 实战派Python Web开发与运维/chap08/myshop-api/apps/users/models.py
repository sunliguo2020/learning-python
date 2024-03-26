from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    SEX = (
        (0, '男'),
        (1, '女'),
    )
    LEVEL = (
        (1, '寂寞卡会员'),
        (2, '钻石卡会员'),
        (3, '金卡会员'),
        (4, '银卡会员'),
    )
    STATUS = (
        (0, '正常'),
        (1, '异常'),
    )

    truename = models.CharField('真实姓名', blank=True, max_length=50)
    mobile = models.CharField('手机号码', max_length=11, default="")
    sex = models.IntegerField('性别', default=0, choices=SEX)
    birthday = models.DateField('生日', blank=True, null=True)
    user_img = models.ImageField("头像", upload_to="user_img", default="", null=True, blank=True)
    level = models.IntegerField('等级', default=4, choices=LEVEL)
    status = models.IntegerField('状态', default=0, choices=STATUS)
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        permissions = (
            ['check_myuser', '审核用户信息'],
        )
