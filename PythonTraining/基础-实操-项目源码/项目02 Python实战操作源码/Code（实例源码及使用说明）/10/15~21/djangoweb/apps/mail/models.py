from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

# Create your models here.


class User(AbstractUser, BaseModel):
    """用户模型类"""

    phone = models.CharField(max_length=20, verbose_name='手机号码')

    class Meta:
        db_table = 'mail_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
