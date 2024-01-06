from django.db import models


# Create your models here.
class Books(models.Model):
    id = models.CharField(primary_key=True, max_length=20, verbose_name='图书编号')
    name = models.CharField(max_length=20, verbose_name='图书名称')
    status = models.BooleanField(default=False, verbose_name='是否出借',blank=True)

    class Meta:
        db_table = 'books'
        verbose_name = '图书表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Record(models.Model):
    book = models.ForeignKey("Books", on_delete=models.CASCADE, verbose_name='书籍')
    name = models.CharField(verbose_name='借书人', max_length=20)
    # 设置auto_created，数据创建时自动设置为当前时间
    s_time = models.DateTimeField(auto_now_add=True, verbose_name='借书时间')
    e_time = models.DateTimeField( auto_now=True, verbose_name='还书时间')
    status = models.BooleanField(verbose_name='是否归还',default=False)

    class Meta:
        db_table = "record"
        verbose_name = '借还记录表'
        verbose_name_plural = verbose_name

