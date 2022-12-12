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


class DepartInfo(models.Model):
    id = models.AutoField(verbose_name='部门编号', primary_key=True)
    departname = models.CharField(verbose_name='部门名称', max_length=30)
    createdate = models.DateTimeField(verbose_name='创建日期',
                                      db_column='createDate')


class UserExtraInfo(models.Model):
    id = models.AutoField(verbose_name='扩展编号', primary_key=True)
    username = models.CharField(verbose_name='用户名称', max_length=30, )
    truename = models.CharField(verbose_name='真实姓名', max_length=30)
    password = models.CharField(verbose_name='密码', max_length=20)

    # 返回两张表的外键user
    user = models.OneToOneField(UserBaseInfo, on_delete=models.CASCADE)
    depart = models.ForeignKey(DepartInfo, default='', on_delete=models.DO_NOTHING)


class SkillInfo(models.Model):
    id = models.AutoField(verbose_name='技能编号', primary_key=True)
    skillname = models.CharField(verbose_name='特长', max_length=30)
    createdate = models.DateTimeField(verbose_name='创建日期',
                                      db_column='createDate')
    user = models.ManyToManyField(UserExtraInfo, db_table='user_skill')
