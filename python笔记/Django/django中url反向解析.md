## **前言介绍**

Django中进行URL反向解析一般有以下三种方式

- • 在模板中使用 `{% url 'blog:detail' post.id %}`的方法
- • 在view视图中一般使用`reverse()` 函数
- • 还有一种特殊情况下使用 `get_absolute_url`的方法

上面三种方式都可以帮助替代`硬编码`简化程序维护成本

## **模板中使用url 标签**

用法很简单，同时也是支持多个参数，比如博客中常用到的

```text
# 无参数，访问博客首页
{% url 'blog:index' %}

# 一个参数，访问指定ID的博客详情页
{% url 'blog:detail' post.id %}
```

上面中的`blog:index`格式中

- • blog 是在APP下的url.py中定义的`app_name` ，一般配合项目urls.py 路径中的namespace 使用

```text
# project/urls.py
urlpatterns = [
    ... ...,
    path('blog/', include('blog.urls', namespace='blog')),
]

# blog/urls.py
app_name = 'blog'
urlpatterns = [
    ... ...,
    path('', views.index, name='index'),
    path('post/<int:id>/', views.detail, name='detail'),
]
```

- • detail 是具体URL path的别名

比如上述代码中的 `name='index'` 和 `name='detail'`，这样做的好处就是如果URL path 路径发生了变化，那么也不用去template模板中修改对应的URL地址，因为`name 没有变`

## **view视图中使用reverse函数**

reverse的目的和template使用url标签是一样的，只是用的位置不一样而已（url标签在template模板，而reverse在view 视图代码中）

- • 使用URL 别名

```text
>>> from django.urls import reverse
>>> reverse('blog:home')
'/blog/'
>>> reverse('blog:archive')
'/blog/archive/'
```

- • 使用view函数名

官网教程提示可以使用 view视图函数名 (`reverse(views.home)`)来解析，但是实际测试是报错 `django.urls.exceptions.NoReverseMatch: Reverse for 'blog.views.home' not found. 'blog.views.home' is not a valid view function or pattern name.`

- • 如果带参数的话，可以使用 args 和 kwargs

```text
>>> from django.urls import resolve
>>> reverse('blog:detail', args=(2, ))
'/blog/post/2/'
>>> reverse('blog:detail', kwargs={'id': 2})
'/blog/post/2/'
```

参考[https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#django.urls.reverse](https://link.zhihu.com/?target=https%3A//docs.djangoproject.com/en/4.1/ref/urlresolvers/%23django.urls.reverse)

## **get_absolute_url定义和使用**

先说`get_absolute_url`的定义，是在对应的Model下，比如Post文章Model

```text
class Post(models.Model):
    ... ...
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:detail', args=(self.id, ))
```

其实这里也看到它其实借用了 `reverse`来实现，那么问什么要单独定义这么个函数呢？

原因在于

1、在VIew视图中如果使用`redirect`进行跳转的话，使用直接使用`对象`，方便很多

```text
from django.shortctus import redirect

def comment(request, post_id):
    post = Post.objects.get(id=post_id)
    # comment 逻辑，评论成功则返回到对应的文章详情页
    return redirect(post)
```

2、在template模板中可以使用 `{{ post.get_absolute_url }}` 来代替 `{% url 'blog:detail' post.id %}`

3、扩展： 后续如果学习了 django restframework 之后，在使用viewset的时候，详情页的返回也是默认调用 `get_absolute_url`的

发布于 2022-10-11 14:15