from django.db import models


# Create your models here.

# create database gx_day16 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题', max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='用户名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name="入职时间")
    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    # 有约束
    # to 与哪张表关联
    # to_field 表中哪一列关联
    # 级联删除
    # dpart = models.ForeignKey(to="Department",to_field='id',on_delete=models.CASCADE)
    # 置空
    dpart = models.ForeignKey(verbose_name="部门名", to="Department", to_field='id', null=True, blank=True,
                              on_delete=models.SET_NULL)
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    price = models.IntegerField(verbose_name='价格',default=0,null=True,blank=True)
    level_choices = (
        (1, '1级'),
        (2, '2级'),
        (3, '3级'),
    )
    level = models.SmallIntegerField(verbose_name="等级",choices=level_choices, default=1)
    status_choice = (
        (1, "已占用"),
        (2, "未占用"),
    )
    status = models.SmallIntegerField(choices=status_choice, verbose_name="状态",default=2)
