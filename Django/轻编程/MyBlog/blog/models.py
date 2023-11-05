from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """ 博客的分类模型 """
    name = models.CharField(max_length=32, verbose_name="分类名称")
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name="分类描述")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    """ 文章标签 """
    name = models.CharField(max_length=10, verbose_name="文章标签")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Post(models.Model):
    """ 文章 """
    title = models.CharField(max_length=61, verbose_name="文章标题")
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name="文章描述")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    content = models.TextField(verbose_name="文章详情")
    tags = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, verbose_name="文章标签")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")   # 手动热门推荐

    pv = models.IntegerField(default=0,verbose_name="浏览量")  # 浏览量
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
    
