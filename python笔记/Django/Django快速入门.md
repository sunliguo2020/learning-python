### 一、Django快速入门

#### Django来源

#### MVT介绍

- Model 模型和数据进行交互
- V:View 视图接收请求
- T：Template 

#### 1、项目创建

```
django-admin startproject 
```

# 二、模型

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
    # 默认模板名为 小写模型类_list.html
    template_name = 'person_list.html'
```

模板person_list.html

```python

{% for item in object_list %}
{% endfor %}

```

CreateView

```python
class PersonCreate(CreateView):
    form_class = PersonCreateForm
    model = Person
    template_name = 'personal_info/person_create.html'
    success_url = reverse_lazy('personal_info:person_list')
```



##### 分页

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



#### django_filter 使用

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


```

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

# 六、应用小案例

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

