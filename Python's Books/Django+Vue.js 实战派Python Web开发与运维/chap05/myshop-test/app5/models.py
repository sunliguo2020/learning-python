from django.db import models


# Create your models here.
class ImgFile(models.Model):
    name = models.CharField(verbose_name='用户名称',
                            default='',
                            max_length=30,
                            )
    headimg = models.FileField(verbose_name='文件名',
                               upload_to="uploads/", null=False, blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '头像信息'
        db_table = 'user_img'
