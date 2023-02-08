from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Article'
        ordering = ['-publish']


    def __str__(self):
        return self.title
