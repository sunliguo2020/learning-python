from django.db import models


# Create your models here.
class UserBaseInfo(models.Model):
    """
    人员基本信息
    """
    id = models.AutoField(verbose_name='编号', primary_key=True)
    username = models.CharField(verbose_name='用户名称', max_length=30)
    password = models.CharField(verbose_name='密码', max_length=20)
    status = models.CharField(verbose_name='状态', max_length=1)
    createdate = models.DateTimeField(verbose_name='创建日期', db_column='createDate')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False  # 不做数据迁移等操作
        verbose_name = '人员基本信息'  # 显示信息
        db_table = 'UserBaseInfo4'  # 设置数据库中的表名


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
