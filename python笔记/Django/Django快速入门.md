# 一、Django快速入门

#### Django来源

#### MVT介绍

- Model 模型和数据进行交互
- V:View 视图接收请求
- T：Template 

#### 1、项目创建

```
django-admin startproject mysite
```

```
django-admin startproject mysite .
```

#### 2、创建应用

```
python manage.py startapp blog
```

多个app创建在一个目录中apps，在apps新建目录blog，startapp 指定这个目录。

```
mkdir apps/blog
python manage.py startapp apps/blog/
```

settings.py 中配置

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # 权限管理
    'django.contrib.contenttypes',  # 内容类型，用于管理模型
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',  # 过滤
    'corsheaders',  # 跨域
    'app1.apps.App1Config',
    'apps.shbz.apps.ShbzConfig',
    'apps.user.apps.UserConfig',
    'apps.get.apps.GetConfig',
    'apps.blog',
    'api',
    'users',
]

```

修改apps/blog/apps.py

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'

```

#### 如何管理静态文件（如图片、JS、CSS）

##### 配置静态文件

1、确保INSTALLED_APPS 包含了django.contrib.staticfiles

2、

```
STATIC_URL = 'static/'
```

3、在模板文件中

```
{% load static %}
<img src="{% 'my_app/example.jpg' %}">
```

4、将静态文件保存在程序中名为static的目录中。例如my_app/static/my_app/example.jpg

你的工程可能包含未与任何应用绑定的静态资源。处了在apps中使用static/目录，你可以在配置摁键中定义一个目录列表（STATICFILES_DIRS),Django会从中寻找静态文件。

```
STATICFILES_DIRS = [
BASE_DIR / 'static',
"/var/www/static/",
]
```



# 二、模型

Django的模型（Model）的本质是类，并不是一个具体的对象（Object）。当你设计好模型后，你就可以对Model进行实例化从而创建一个一个具体的对象。Django对于创建对象提供了2中不同的save与create方法。

Person模型类：

```python
from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
```

#### 用save方法创建对象

只有你用来save方法后，Django才会将这个对象的信息存储到数据库中。

```
lucifer = Person(name='lucifer')
lucifer.save()
```

用create方法创建对象。使用create方法，无需再加上save。create不经创建的新的对象，而且直接将信息存储到数据库里。

```
lucifer = Person.objects.create(name='lucifer')
```



#### 3、后台管理

admin.py

```
admin.site.register()
```

# 三、视图

## 1、视图的基本使用

视图函数的例子

视图函数定义的基本要求：

​	1、视图函数必须定义一个参数（通过命名request）

​	request参数：用来接收客户端的请求信息

​	2、视图函数的返回值必须是一个HttpResponse对象（或者是子类）

视图使用的流程：

​	1.在应用的views.py定义视图函数

​	2、配置路由

​		1）在项目的urls.py中关联应用下的urls.py

​			from django.contrib import admin

​			from django.urls import path,include,re_path

​			urlpatterns = [

​			#将应用中的urls文件包含进来

​			re_path(r'^news/',include('news.urls'))

​			]

​	2)	在应用的目录下定义一个urls.py文件

​	3） 配置具体的访问规则

​			from django.urls import path

​			from .views import index

​			urlpatterns = [    path('index/', index),]

##### 视图函数定义基本步骤：

​	1、获取查询参数

​	2、得到queryset

​	3、分页数据

​	4、返回context 

​	5、模板遍历context['queryset']

```python
def personid_list(request):
    """
    get_getpersonid 表的展示
    :param request:
    :return:
    """
    search_data = request.GET.get('q', '')
    logging.debug(f'查询的参数为{search_data}')
    if search_data:
        queryset = models.GetPersonId.objects.filter(idcard__icontains=search_data)
    else:
        queryset = models.GetPersonId.objects.all()

    page_obj = Pagination(request, queryset)

    context = {
        'queryset': page_obj.page_queryset,
        'page_string': page_obj.html(),
    }

    return render(request, 'get/personid_list.html', context)
```



###### 类视图的使用步骤：

from django.views import View

1、定义一个类，继承Django的View类

```python
class NewSView(View):
	def get(self,request):
        pass
    def post(self,request):
        pass
```

2、在url.py中配置路由

 

​	2、配置URL

​	3、请求访问

​	4、返回模型类定义的数据

### 增 视图

```python
def person_add(request):
    """
    手动添加人员信息
    :param request:
    :return:
    """
    if request.method == "GET":
        # 通过get 添加用户
        if request.GET:
            form = PersonModelForm(request.GET)
        else:
            form = PersonModelForm()
        context = {"form": form}
        return render(request, 'change.html', context)
    if request.method == "POST":
        form = PersonModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('app1:person_list'))
        context = {"form": form}
        return render(request, 'change.html', context)

```



#### 五大视图

| 动作 | 视图名               | 是否需要Model | 是否需要Form |
| ---- | -------------------- | ------------- | ------------ |
| 增   | CreateView           | 是            | 是           |
| 删   | DeleteView           | 是            | 否           |
| 改   | UpdateView           | 是            | 是           |
| 查   | ListView，DetailView | 是            | 否           |

ListView（TempLateView）

```python
class PersonListView(ListView):
    model = Person
    # 默认模板名为 小写模型类_list.html   <appname>/<modelname>_list.html
    template_name = 'person_list.html'
    # 默认为model_name+_list  模型名称小写+_list 
    context_object_name = 'xxx_list'
    # 默认为None，不分页
    paginate_by =10
```

模板person_list.html

```python

{% for item in object_list %}
{% endfor %}

```

#### context

object_list 都有这个属性

```python
context = {
	'object_list':queryset,
	# 手动设置或者默认
	context_object_name :queryset,
}
```



```python
    def get_context_data(self, *, object_list=None, **kwargs):
        """Get the context for this view."""
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(
                queryset, page_size
            )
            context = {
                "paginator": paginator,
                "page_obj": page,
                "is_paginated": is_paginated,
                "object_list": queryset,
            }
        else:
            context = {
                "paginator": None,
                "page_obj": None,
                "is_paginated": False,
                "object_list": queryset,
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super().get_context_data(**context)
```



CreateView

```python
class PersonCreate(CreateView):
    form_class = PersonCreateForm
    model = Person
    template_name = 'personal_info/person_create.html'
    success_url = reverse_lazy('personal_info:person_list')
```



## 分页

### Paginator对象

负责分页数据整体的管理

对象的构造方法

```python
# def __init__(self, object_list, per_page, orphans=0, allow_empty_first_page=True):
paginator = Paginator(object_list,per_page)
# 参数 - object_list 需要分页数据的对象列表
		# per_page 每页数据个数
```

## Page对象

负责具体某一页的数据的管理

创建对象

​	Paginator对象的page()方法返回Page对象

​	page = paginator.page(页码)

Page对象属性：

	- object_list :当前页上所有数据对象的列表
	- number：当前页的序号，从1开始
	- paginator：当前page对象相关的Paginator对象

Page对象方法：

- has_next()	如果有下一页返回True
- has_previous() 如果有上一页返回True
- has_other_pages()     如果有上一页或下一页返回True
- next_page_number() 返回下一页的页码
- previous_page_number() 返回上一页的页码



##### 函数视图中使用分页

以博客为例，在Django视图函数中使用Paginator类对首页文章列表进行分页。它会向模板传递2个重要参数：

1. `page_obj`: 分页后的对象列表，在模板中使用for循环遍历即可；

2. `is_paginated`: 可选参数。当总页数不超过1页，值为False，此时模板不显示任何分页链接 。

   ```python
   from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
   from .models import Article
   from django.shortcuts import render
   
   def article_list(request):
       queryset = Article.objects.filter(status='p').order_by('-pub_date')
       paginator = Paginator(queryset, 10)  # 实例化一个分页对象, 每页显示10个
       page = request.GET.get('page')  # 从URL通过get页码，如?page=3
       try:
           page_obj = paginator.page(page)
       except PageNotAnInteger:
           page_obj = paginator.page(1) # 如果传入page参数不是整数，默认第一页
       except EmptyPage:
           page_obj = paginator.page(paginator.num_pages)
       is_paginated = True if paginator.num_pages > 1 else False # 如果页数小于1不使用分页
       context = {'page_obj': page_obj, 'is_paginated': is_paginated}
       return render(request, 'blog/article_list.html', context)
   ```



##### 基于类的视图中使用分页

在基于类的视图`ListView`中使用分页，只需设置`paginate_by`这个参数即可。它同样会向模板传递`page_obj`和`is_paginated`这2个参数。

```python
from django.views.generic import ListView
from .models import Article

class ArticleListView(ListView):
    queryset = Article.objects.filter(status='p').order_by('-pub_date')
    template_name = "blog/article_list.html"
    paginate_by = 10 # 每页10条
```



##### 展示分页链接的通用模板

这里提供了两种展示分页链接的通用模板，对基于函数的视图和类视图都是适用的。当`is_paginated=True`时展示分页链接。

方式1： 上一页, Page 1 of 3, 下一页

```html
 <ul> 
{% for article in page_obj %} 
   <li>{{ article.title }}</li> 
{% endfor %}
</ul>

{% if is_paginated %}
<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">上一页</a>
        {% endif %}

        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">下一页</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>
{% endif %}
```

方式2： 上一页, 1, 2, 3, 4, 5, 6, 7, 8, … 下一页。本例加入了Bootstrap 4的样式美化（推荐)。

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
 
{% if page_obj %}
    <ul> 
    {% for article in page_obj %}
       <li> {{ article.title }</li>
     {% endfor %}
   </ul>

   {# 分页链接 #}
   {% if is_paginated %}
     <ul class="pagination">
    {% if page_obj.has_previous %}
      <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a></li>
    {% else %}
      <li class="page-item disabled"><span class="page-link">Previous</span></li>
    {% endif %}
 
    {% for i in page_obj.paginator.page_range %}
        {% if page_obj.number == i %}
      <li class="page-item active"><span class="page-link"> {{ i }} <span class="sr-only">(current)</span></span></li>
       {% else %}
        <li class="page-item"><a class="page-link" href="?page={{ i }}">{{ i }}</a></li>
       {% endif %}
    {% endfor %}
 
      {% if page_obj.has_next %}
      <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a></li>
    {% else %}
      <li class="page-item disabled"><span class="page-link">Next</span></li>
    {% endif %}
    </ul>
    {% endif %}
 
{% else %}
{# 注释: 这里可以写自己的句子 #}
{% endif %}
```

例三：

```
{% if is_paginated %}
  <ul class="pagination">
      {% if page_obj.has_previous %}
          <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a>
           </li>
      {% else %}
         <li class="page-item disabled"><span class="page-link">Previous</span></li>
       {% endif %}
		
		{% for i in paginator.page_range %}
           {% if page_obj.number == i %}
             <li class="page-item active"><span class="page-link"> {{ i }} <span
                  class="sr-only">(current)</span></span>
               </li>
            {% else %}
               <li class="page-item"><a class="page-link" href="?page={{ i }}">{{ i }}</a></li>
        {% endif %}
         {% endfor %}

       {% if page_obj.has_next %}
         <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a>
           </li>
        {% else %}
         <li class="page-item disabled"><span class="page-link">Next</span></li>
          {% endif %}
      </ul>

        {% endif %}
```



#### ListView

```python
class PersonidListView(ListView):
    """
    通过继承ListView的方式，以列表的形式展示personid
    """
    model = models.PersonId
    allow_empty = False
    ordering = ['-id']
    filter_class = PersonIdFilter
    http_method_names = ['get']  # 加上这一行，告知允许那种请求方式
    # 模板文件
    template_name = 'app1/personid_list2.html'
    # 每页显示的条数
    """
     Paginator常用属性和方法：
            count：总共有多少条数据。
            num_pages：总共有多少页。
            page_range：页面的区间。比如有三页，那么就range(1,4)。
        Page常用属性和方法：
            has_next：是否还有下一页。
            has_previous：是否还有上一页。
            next_page_number：下一页的页码。
            previous_page_number：上一页的页码。
            number：当前页。
            start_index：当前这一页的第一条数据的索引值。
            end_index：当前这一页的最后一条数据的索引值。
    """
    paginate_by = 10

    # 设置模板变量的上下文，如果没有设置context_object_name的值，那么
    # 模板变量上下文名称由 "模型名称的小写+_list"组成。
    context_object_name = "personids"

    # 查询的数据，不写默认查询指定模型的所有数据
    queryset = models.PersonId.objects.filter(is_delete=0)

    def __init__(self, ):
        self.filter = None

    def get_queryset(self):
        queryset = super().get_queryset()
        # 创建了一个过滤器实例，并通过调用filter.qs获取了过滤后的查询结果。
        self.filter = self.filter_class(self.request.GET, queryset=queryset)
        return self.filter.qs

    # 还重写了get_context_data方法，将过滤器实例添加到上下文中，以便在模板中使用。
    # 这样，我们就可以在模板中直接使用过滤器的属性和方法来展示搜索结果。
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 实现过滤  filter.form 展示查询的表单
        context['filter'] = self.filter

        # 实现分页  当前页前后几页显示
        context['max_left_item_count'] = 10

        return context
```



# django_filter 使用

###### 1、安装

```python
pip install django-filter
```

###### 2、settings.py设置

```python
INSTALL_APPS = [
    'django_filters'
]
```

###### 3、filters.py自定义过滤类 

```python
import django_filters

from . import models


class GetDaglpersonFilter(django_filters.FilterSet):
    personid = django_filters.CharFilter(field_name='personid', label='personid')

    class Meta:
        model = models.GetDaglperson
        # fields = ['personid']
        fields = {
            # 'personid': ['icontains']
        }
                fields = {
            			'title': ['icontains'],
						'category__name': ['icontains'],
						'pub_date': ['year__gt'],
						}

```

我们创建Filter类时，不仅要指定筛选字段，而且要需要指定该字段的匹配查询方式(lookup_expr)。如果不指定，Filter类默认都是使用"exact"精确匹配的.

###### 4、视图中使用

```python

class DaglpersonView(View):
    def get(self, request):
        f = GetDaglpersonFilter(request.GET, queryset=models.GetDaglperson.objects.all())
        context = {
            'filter': f
        }
        return render(request, 'get/daglperson_list.html', context)
```

> 
>
> 每个f包含两个属性，f.form 申城筛选表单，f.qs包含筛选结果集。

5、模板中使用f.form,f.qs

```
{% extends "blog/base.html" %}
<h3>搜索文章</h3>
{% block content %}
    <form action="" method="get">
{{ filter.form.as_p }}
        <input type="submit" />
    </form>
<ul>
{% for obj in filter.qs %}
     <li>{{ obj.title }}, 类别: {{ obj.category.name }}</li>
{% endfor %}
</ul>
{% endblock %}
```

美化filter类

```
class ArticleFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name='title',lookup_expr='icontains', label="关键词")
    category = django_filters.ModelChoiceFilter(
        field_name='category', queryset=Category.objects.all(),
)
    pub_date__gte = django_filters.NumberFilter(field_name='pub_date',
lookup_expr='year__gte', label="发表年份>=")

    class Meta:
        model = Article
        fields = {
        }
```



ListView中使用 重写get_queryset()

```python
   def get_queryset(self):
        queryset = super().get_queryset()
        # 创建了一个过滤器实例，并通过调用filter.qs获取了过滤后的查询结果。
        self.filter = self.filter_class(self.request.GET, queryset=queryset)
        return self.filter.qs
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 实现过滤  filter.form 展示查询的表单
        context['filter'] = self.filter
        # 实现分页  当前页前后几页显示
        context['max_left_item_count'] = 10

        return context
```



###### 5、模板中使用filter.form 显示查询表单，filter.qs 查询结果

```html
 <form method="get">
     <div class="input-group">
       {{ filter.form.as_p }}
     <button class="btn btn-default" type="submit">
     <span class="glyphicon glyphicon-search " aria-hidden="true"> </span>
      </button>
       </span>
    </div>
 </form>
{% for item in filter.qs %}
```

#### 5、模板

### 文件上传

- 当Django在处理文件上传的时候，文件被保存在request.FILES
- FILES中每个键为<input type='file' name=''/>中的name
- FILES只有在请求的方法为POST且提交的<form>中带有enctype='multpart/form-data'的情况下才包含数据

### 分页操作

Django提供了一些类实现管理数据分页

- Paginator对象

  ​	Paginator(列表，int) 返回分页数据，参数为列表数据，每页数据的条数

  - 属性

    count:对象总数

    num_pages:页面总数

    page_range:页面列表，从1开始，例如：[1,2,3,4]

  方法

  page(num):下标从1开始，如果提供的页面不存在，抛出InvalidPage异常。
  
## 2、路由

  

## 3、错误视图

  Django内置处理HTTP错误的视图，主要错误及视图包含：

  - 404：url匹配失败，找不到页面
  - 500：server error视图

### 1、404错误视图配置

  将请求的地址进行url匹配后，没有找到匹配的正则表达式，则调用404视图。 

## 4、HttpRequest 对象

1、reuqest对象属性

- path				请求路径
- method          请求方法
- encoding        请求体参数编码
- GET
- POST
- FILES
- COOKIES



2、案例演示

3、QueryDict对象

HttpRequest对象的属性GET、POST都是QueryDIct类型的对象，与python字典不通，QueryDict类型的对象用来处理同一个键带有多个值的情况。

#### 	1、方法get()

- 根据键取值，如果一个键同时拥有多个值将获取最后一个值
- 如果不存在则返回None值，可以设置默认值进行后续处理

```
dict.get('键',默认值)
```

#### 2、方法getlist()

- 根据键取值，值以列表返回，可以获取指定键的所有值
- 如果键不存在则返回空列表[]，可以设置默认值进行后续处理。



4、GET属性

GET属性是一个QueryDict类型的对象，键和值都是字符串类型



5、POST属性

## 5、HttpResponse对象

视图在接收请求处理后，必须返回HttpResonse对象或子对象

## 1、初始化参数

- content：返回的 内容字符串
- charset：表示response采用的编码字符集，默认为utf-8
- status_code:返回的http响应状态码
- content-type：指定返回数据的MIME类型，默认为'text/html'

### 2、常用方法

- set_cookie:

>设置Cookie信息
>
>```
>set_cookie(key,value='',max_age=None,expires=None)
>```
>
>- max_age 整数，表示在指定秒后过期
>
>- expires是要给datetime或timedelta对象，会话将在这个指定的日期/时间过期
>
>- max_age与expires二选一
>
>- 如果不指定过期时间，在关闭浏览器时cookie会过期。
>
>- write：向响应体中写数据。
>
>  

- delete_cookie:

  >删除值当key的cookie
  >
  >```
  >delete_cookie(key)
  >```

### 3、JsonResponse

JsonResponse是HttpResponse的子类，用来返回json数据。JsonResponse对象返回的content-type为'application/json'

## 6、登录案例

## 7、cookie和session

# 四、模板

### Form基础介绍

首先让我们先来了解下 Django 中 Form 表单的基本用法。Django 中提供了两种 Form 表单类型，一种是 forms.Form ，另外一种是 forms.ModelForm 。很明显，一种是普通的 Form 表单类型，另外一种是和 Model 有关联的表单类型。

对于 Django 中的 Form 表单的用法，我们只需要了解以下几点：

1. 它是一个定义一个 Form 类，基类是 django.forms.Forms 或者 django.forms.ModelForm ，在 view 中实例化定义好的 Form 类，在模板中使用 {{ form }} 即可自动生成对应的 form 表单内容。
2. ModelForm 比较简单，它适用于：当你创建的表单内容与某个 Model 内容很相似的情况。如上面文档介绍的一样
3. 在 Form 类中，clean 方法可以在做表单验证，它是一个总的验证方法。clean_xxx 是单个表单验证方法，其中 xxx 是对应的属性名称
4. form.clean_data 是会得到字典类型，key 是对应属性名，value 即为表单输入的值
5. 生成的 form 标签，id 是有特殊规律的，我们可以通过这些 id 进行一些 js 操作

#### forms.Form 的初始化 

#### forms模板写法

第一种：

```python
<form method="POST" class="form-horizontal" role='form' action="#" novalidate>
    {% csrf_token %}
    {{ form.as_p }}
    <div class="form-group">
        <div class="col-md-6">
            <button type="submit" class="button-form ">开始爬取</button>
        </div>
    </div>
</form>
```

第二种：

```html

<form action="" method="post" class="form-signin" novalidate>
    <div class="content">
        {% for item in user_form %}
        {% csrf_token %}
        <div class="form-group">
            <label for="{{ item.id_for_label }}">{{ item.label }}:</label>
            {{ item }}
            <div class="invalid-feedback">{{ item.help_text }}</div>
            {% if item.errors %}
            <span style="color:red;">{{ item.errors.0 }}</span>
            {% endif %}
        </div>
        {% endfor %}

        <div class="form-group">
            <buttontype="submit" class="btn btn-primary"> 注册</button>
        </div>

        <small>已有账号?</small>
        <a href={% url 'account:account_login' %} class="signup">&nbsp;登录</a>
    </div>
</form>
```

#### form css属性

第一种方法：重写__init__(self)方法

第二种方法：设置widgets属性

```python
class PersonIdModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加 class=“form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": '请输入 ' + field.label}
        self.fields['idcard'].widget.attrs.update({'class': 'form-control', 'placeholder': '请输入身份证号'})

    class Meta:
        model = PersonId
        fields = ['personid', 'idcard']
        labels = {
            'personid': '个人ID'
        }
        widgets = {"link_phone1": forms.TextInput(attrs={"class": "form-control",
                                                         'placeholder': '请输入手机号码'})}

    def clean_idcard(self):
        idcard = self.cleaned_data.get('idcard')
        if len(idcard) != 18:
            raise forms.ValidationError('身份证少于18位')
        return idcard
```

#### Form的save(commit=False)方法和save_m2m()方法

首先说明save(commit=False)和save_m2m()都是form表单的方法。

django中有时候需要使用form.save(commit=False)方法，更新对象属性，但并不向数据库真正提交数据，举个博客的例子吧，登录之后，写博客，然后保存博客的内容。博客的有些内容是在界面上由用户填写的，有些内容是在后台添加的。例如，用户姓名之类的。

　　这样的话就需要在form.save()方法中传递一个参数commit，赋值为False，代表不要提交到数据库。然后给blog.author=request.user赋值，然后有两种选择：

　　1. 调用new_blog.save()保存blog的基本信息，然后在调用form.save_m2m()保存关联信息(外键字段)。

　　2. 再一次调用form.save()保存blog基本信息以及关联信息。




## **问题总结**

### 判断用户是否登录

1、is_authenticated方法

 is_authenticated 属于Django User对象中的一个方法，只是Django在内部通过装饰器@property将该方法装饰为可被User对象调用的一个属性。 

```python
  @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
```

2.is_authenticated方法的实现过程：
用户在登录过后，Django会将用户的id以及use_backen写入到session会话，以一定的有效期存入数据库或者缓存中。并在登录响应cookie中写入一个sessionid=xxxxxxxxx的值。当用户访问用户中心（或其他需要登录才能访问的页面时），我们在视图中调用的request.user.is_authenticated方法就会去获取当前请求对象cookie中sessionid=xxxxx的值，然后通过’xxxx‘这个值去数据库或者缓存中找到当前这个’xxxx’值对应的记录值，然后判断用户登录或存在。

 3.返回值：True,False 

```python
# 路由
path('auth/', AuthenticatedView.as_view()),
# 视图
class AuthenticatedView(View):
    def get(self, request):
    	# 判断用户是否登录
        if not request.user.is_authenticated:
            return http.JsonResponse({
                'errmsg': '用户未登录'
            })
        return http.JsonResponse({
            'errmsg': '登录成功',
        })

```



## 1、基本需求

### 1、功能图

2、数据库表结构

- 用户表（user）

| 字段名   | 类型 | 说明   |
| -------- | ---- | ------ |
| id       | int  | 主键   |
| username | str  | 用户名 |
| password | str  | 密码   |

- 书籍表（Books)

| 字段名 | 类型 | 说明             |
| ------ | ---- | ---------------- |
| id     | str  | 书籍编号（唯一） |
| name   | str  | 书籍名           |
| status | bool | 是否出借         |

- 借还记录表（Record）

| 字段名 | 类型     | 说明                                   |
| ------ | -------- | -------------------------------------- |
| id     | int      | 主键                                   |
| book   | int      | 书籍（id）                             |
| sdate  | datetime | 借书时间                               |
| name   | str      | 借书人                                 |
| e_date | datetime | 归还时间（默认为借书时间，归还后才有） |

2、创建项目

3、模型类实现

### 4、接口实现

#### 1、登录接口

表单请求方式：

```
POST /user/login/ HTTP/1.1
User-Agent: PostmanRuntime/7.33.0
Accept: */*
Cache-Control: no-cache
Postman-Token: 1c655798-2ac7-4b1f-a32e-b5016f3650d2
Host: 127.0.0.1:8000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 35

username=username&password=password
```



GET 请求

```
GET /user/login/?username=username&password=password HTTP/1.1
User-Agent: PostmanRuntime/7.33.0
Accept: */*
Cache-Control: no-cache
Postman-Token: 6cdbc8df-9c77-4813-819d-3124b1efd3b9
Host: 127.0.0.1:8000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 35

username=username&password=password
```



json

```
POST /user/login/ HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.33.0
Accept: */*
Cache-Control: no-cache
Postman-Token: ae17b29b-ed89-4a84-92db-4850f477180a
Host: 127.0.0.1:8000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59

{
    "username":"username",
    "password":"password"
}HTTP/1.1 200 OK
Date: Fri, 06 Oct 2023 05:01:49 GMT
Server: WSGIServer/0.2 CPython/3.10.5
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 49
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"code": 200, "username": null, "password": null}
```

```python
class LoginView(View):
    def post(self, request):
        """登录接口
        获取参数（表单/json)
        request.POST 获取表单参数
        request.body 获取json数据
        """

        # 获取参数
        params = request.POST if len(request.POST) else json.loads(request.body.decode('utf-8'))

        username = params.get('username')
        password = params.get('password')

        # 校验账号密码是否正确
        user = authenticate(username=username,password=password)
        if user:
            # 保存登录的信息到session
            login(request, user)
            return JsonResponse({'code': 1000, "message": "登录成功"})
        else:
            return JsonResponse({'code': 2001, "message":"登录失败，账号或密码不对！"},status='403')

```

