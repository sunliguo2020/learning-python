from django.db import models
from django.utils import timezone


# Create your models here.

# create database gx_day16 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
class Department(models.Model):
    """部门表"""
    title = models.CharField(unique=True, verbose_name='标题', max_length=32)

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
    price = models.IntegerField(verbose_name='价格', default=0, null=True, blank=True)
    level_choices = (
        (1, '1级'),
        (2, '2级'),
        (3, '3级'),
    )
    level = models.SmallIntegerField(verbose_name="等级", choices=level_choices, default=1)
    status_choice = (
        (1, "已占用"),
        (2, "未占用"),
    )
    status = models.SmallIntegerField(choices=status_choice, verbose_name="状态", default=2)


class Shoujihao(models.Model):
    """
    联通手机号信息
    """
    PROD_INST_ID = models.CharField(max_length=32)
    CUST_ID = models.CharField(max_length=32, null=True, blank=True, )
    LATN = models.CharField(max_length=32, verbose_name='区号')
    BUSI_NBR = models.CharField(max_length=32, verbose_name='号码', db_index=True)
    USER_NAME = models.CharField(max_length=32, db_index=True)
    CUST_NAME = models.CharField(max_length=32, db_index=True)
    INSTALL_ADDR = models.CharField(max_length=32, null=True, blank=True, verbose_name="安装地址")
    CERTIFICATES_NBR = models.CharField(max_length=32, verbose_name="身份证号", db_index=True)
    mod_time = models.DateTimeField(verbose_name="修改时间", db_index=True)
    is_active = models.BooleanField(verbose_name="删除标志", default=True)


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class Task(models.Model):
    """"任务"""
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),

    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name='负责人', to='Admin', on_delete=models.CASCADE)


class Webcam(models.Model):
    """
    监控截图管理
    """
    ipaddr = models.CharField(verbose_name="ip地址", max_length=16)
    file_name = models.CharField(verbose_name="文件名", max_length=16, default=None)
    file_path = models.CharField(max_length=64)
    capture_date = models.DateTimeField(verbose_name="截图时间")
    school = models.ForeignKey(to="School", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="学校")


class School(models.Model):
    """
    学校信息
    """
    school_name = models.CharField(max_length=12)

    def __str__(self):
        return self.school_name


class WebcamPic(models.Model):
    file_name = models.CharField(verbose_name="文件名称", max_length=128,unique=True)
    img = models.FileField(verbose_name='监控截图', upload_to='webcam', default=None)
    create_datetime = models.DateTimeField(verbose_name="上传时间", auto_now_add=True)
    capture_datetime = models.DateTimeField(verbose_name="截图时间",null=True,blank=True)
    ip_addr = models.GenericIPAddressField(null=True)

    class Meta:
        verbose_name = '监控截图'




class Order(models.Model):
    """
    订单
    """
    oid = models.CharField(verbose_name='订单号', max_length=64)
    title = models.CharField(verbose_name='名称', max_length=32)
    price = models.IntegerField(verbose_name='价格')

    status_choices = (
        (1, '未支付'),
        (2, '已支付'),
    )
    status = models.SmallIntegerField(verbose_name='订单状态', choices=status_choices, default=1)
    admin = models.ForeignKey(verbose_name='管理员', to=Admin, on_delete=models.CASCADE)
