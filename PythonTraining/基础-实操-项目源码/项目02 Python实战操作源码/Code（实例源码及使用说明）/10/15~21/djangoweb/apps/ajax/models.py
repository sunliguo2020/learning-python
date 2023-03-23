from django.db import models
from db.base_model import BaseModel

# Create your models here.


class Type(BaseModel):
    """类型模型类"""

    name = models.CharField(max_length=20, verbose_name='种类名称')

    class Meta:
        db_table = 'df_type'
        verbose_name = '种类'
        verbose_name_plural = verbose_name


class TypeDetail(BaseModel):
    """详细类型模型类"""

    type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='种类名称')
    name = models.CharField(max_length=20, verbose_name='具体名称')

    class Meta:
        db_table = 'df_type_detail'
        verbose_name = '具体类型'
        verbose_name_plural = verbose_name
