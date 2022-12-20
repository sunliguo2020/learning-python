from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    photo = models.CharField('用户头像', max_length=50)
    weChat = models.CharField('微信', max_length=30)
    level = models.CharField('用户等级', max_length=1)

    def __str__(self):
        return self.username

    class Meta:
        permissions=(
            ['check_diyuser','审核用户信息'],
        )
