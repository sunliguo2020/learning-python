## **一、关于为何要分页**

当处理大量数据时，如果一次将这些数据查询出来进行响应，必然对服务器内存、负载有所影响，影响低接口响应，进而影响用户体验。 常见的方式是将数据分段展示给用户，如果当前分段中没有需要的数据，那么就可以通过翻页或者指定具体的页码来查看更多的数据。

> Django提供了默认的分页功能，同时也允许自定义分页来满足特定需求。

## **二、Django的默认分页 （函数视图）**

> 在视图中，使用Django提供的Paginator类来分页数据。一般是和Django的Template结合使用

1、需要引入Paginator和要分页的数据模型。

```text
from django.core.paginator import Paginator
from myapp.models import Post
```

2、获取要分页的数据，并创建 Paginator 对象，进行分页设置

```python
# 获取数据
posts = Post.objects.all()

# 创建Paginator对象
# 作为测试这里 per_page 可以小一些
paginator = Paginator(posts, per_page=2)
```

3、或者`指定的页码` 数据， 默认习惯使用 `page` 参数

```text
# 或者当前页码 
page_number = request.GET.get('page', 1)

# 获取 页码对应的数据
page_data = paginator.get_page(page_number)

# 数据渲染到 template模板中去
return render(request, 'posts/list.html', {'page_data': page_data})
```

4、在 Template模板中使用`page_data` 来展示数据和分页导航

```text
<ul>
    {% for post in page_data %}
        <li> {{ post.title }}</li>
    {% endfor %}
</ul>

<br>

<!-- 分页导航 -->
<div class='pagination'>
    {% if page_data.has_previous %}
        <span> 
            <a href="?page=1">&laquo;  首页</a>
            <a href="?page={{ page_data.previous_page_number }}">前一页</a>
        </span>
    {% endif %}
    当前页码: {{ page_data.number }} / {{ page_data.paginator.count }}
    {% if page_data.has_next %}
        <span>
            <a href="?page={{ page_data.next_page_number }}">后一页</a>
            <a href="?page={{ page_data.paginator.num_pages }}">&laquo;  尾页</a>
        </span>
    {% endif %}
</div>
```

实际的效果如下图所示：

![img](https://pic4.zhimg.com/80/v2-7a95e7ac7bda7d520cb9c28b7ae15caf_720w.webp)

Django Template 分页实现demo演示

## **三、Django的默认分页（类视图）**

上面介绍的是在Django的`函数视图`种如何使用分页功能， 这趴介绍在`类视图`中使用分页功能。

如果对Django 函数视图和类视图有过了解的同学就会很容易知道。如何把上面的 函数视图改造成 类视图。

其实很简单，类视图中的`get()`方法的代码逻辑就是上面的 函数视图的代码。如下

```text
class PostListViewDemo(View):
    def get(self, request):
         # 获取数据
        posts = Post.objects.all()

        # 创建Paginator对象
        paginator = Paginator(posts, per_page=3)

        # 或者当前页码 
        page_number = request.GET.get('page', 1)

        # 获取 页码对应的数据
        page_data = paginator.get_page(page_number)
        # 这里输出debug日志，
        print(page_data, type(page_data), dir(page_data))

        # 数据渲染到 template模板中去
        return render(request, 'posts/list2.html', {'page_data': page_data})
```

需要主要的就是在urls中设置路由时。 类视图需要使用 `as_view()` 方法，如下

```text
from django.urls import path 

from appdemo.views import post_list, PostListViewDemo

urlpatterns = [
    path('list1/', post_list, name='post-list-1'),
    # 注意这里
    path('list2/', PostListViewDemo.as_view(), name='post-list-2'),
]
```

## **四、更简单的`Django类视图分页实现`**

我们知道只有在大数据量，也就是 `列举数据`的时候用到分页。

Django在 django.views.generic 中提供了更简便的封装类 `ListView`

上面的分页功能可以很简单的如下实现

```text
from django.views.generic import ListView

from appdemo.models import Post


class PostListView(ListView):
    paginate_by = 4
    model = Post
    # 注意  
    # 如果这里不指定 template_name， 那么默认的值为  appdemo/post_list.html
    # 组成是 app_label, model_name, template_name_suffix(对于ListView而言是 _list.html)
    template_name = "posts/list3.html"
```

这里需要注意的是：

在Template文件 `posts/list3.html` 不能使用前面两种方式中 自定义的 `page_data` 对象 ，而要使用固定格式的 `page_obj` 对象。

具体餐参考 Django源码 `django.views.generic.list.MultipleObjectMixin` 类中的`get_context_data()` 方法的返回

> 源码解释

因为 ListView 继承自 `MultipleObjectTemplateResponseMixin` 和 `BaseListView` ， 在 `BaseListView` 中定义了 `get()` 方法， get方法中调用了 `context = self.get_context_data()` 然后 get 返回 context, 而 `get_context_data()` 方法的定义就是在 `MultipleObjectTemplateResponseMixin` 类中

## **五、关于Django原生自定义分页**

默认情况下，使用 Django+Template 进行前后端结合在一起的开发，Django提供的Paginator类 已经能满足日常需求。

因为 `Page` 对象已经提供了关于`分页操作`的各种情况，这里做个汇总介绍

### **Paginator 属性和方法**

**属性**

- • Paginator.count 返回的是所有页的对象总数
- • Paginator.num_pages 返回的是总的页数
- • Paginator.page_range 返回的是从1到最大页数的迭代器

**方法**

- • Paginator.get_page(page_number)
- • Paginator.Page(page_number)

以上两种方法都是用于获取当前页码对应的数据。不同的是：

***1、返回值不一样***

1.1、`get_page` 返回的是 `Page` 对象，可以通过该对象来访问页码、总页数、当前页的数据等信息。如下面对于 Page的属性和方法的汇总介绍

1.2、`page` 返回的是`QuerySet`对象， 可以像处理普通查询结果集一样处理分页数据。

***2、处理异常情况不一样***

> 如果指定的页码超出了有效范围（小于1或大于总页数）

2.1、`get_page` 方法会返回一个空的Page对象（不会抛出异常）

2.2、`page` 方法会抛出PageNotAnInteger或EmptyPage异常，需要在代码中进行处理。

### **Page 属性和方法**

**属性**

- • Page.object_list 返回的是`当前页码对应的对象列表`
- • Page.number 返回的是当前页码
- • Page.paginator 放回的是对应的`Paginator`对象

**方法**

- • Page.has_next() 当前Page对象是否有下一页
- • Page.has_previous() 当前Page对象是否有上一页
- • Page.has_other_pages() 当前Page对象对应的页码是否有前一页或者后一页，如果有返回True
- • Page.next_page_number() 返回下一页的页码， 下一页不存在则报 InvaliPage
- • Page.previous_page_number() 返回上一页的页码, 上一页不存在则报 InvaliPage
- • Page.start_index() 返回当前页面的第一个对象 在所有对象中的索引值
- • Page.end_index() 返回当前页面的最后一个对象 在所有对象中的索引值

------

今天的知识就介绍到这里， 下一篇我们介绍在进行 Django前后端分离开发中，如何使用分页功能

如果觉得文章对你有用，请不吝点赞 和 关注个人公众号（搜索 全栈运维 或者 DailyJobOps）

附件 django_pagination示例代码下载[1]

### **引用链接**

`[1]` django_pagination示例代码下载: *[http://mp-weixin.colinspace.com/projects/django_pagination.tar.gz](https://link.zhihu.com/?target=http%3A//mp-weixin.colinspace.com/projects/django_pagination.tar.gz)*

发布于 2023-07-06 16:05・IP 属地北京