# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-12 13:01
"""
from django.db import models


class BaseModel(models.Model):
    """
    公共字段模型
    """
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        abstract = True
        verbose_name_plural = "公共字段模型"
        db_table = 'BaseTable'
