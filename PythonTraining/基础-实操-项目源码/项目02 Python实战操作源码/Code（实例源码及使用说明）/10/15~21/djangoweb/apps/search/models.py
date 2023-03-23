from django.db import models


class Poetry(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=50)
    author = models.CharField('作者', max_length=20)
    detail = models.CharField('内容', max_length=300)

    # 设置返回值
    def __str__(self):
        return self.name
