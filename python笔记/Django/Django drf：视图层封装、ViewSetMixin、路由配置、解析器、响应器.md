**本文目录：**

**一、视图层封装**

**二、ViewSetMixin**

**三、路由配置**

**四、解析器**

**五、响应器**

 

# 一、视图层封装

## 1.基本视图

写一个出版社的增删改查resfull接口

路由：

```python
    url(r'^publish/$', views.PublishView.as_view()),
    url(r'^publish/(?P<pk>\d+)/$', views.PublishDetailView.as_view()),
```

视图：

```python
class PublishSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Publish
        fields='__all__'

class PublishView(APIView):

    def get(self, request):
        publish_list = models.Publish.objects.all()
        bs = PublishSerializers(publish_list, many=True)
        # 序列化数据

        return Response(bs.data)

    def post(self, request):
        # 添加一条数据
        print(request.data)

        bs=PublishSerializers(data=request.data)
        if bs.is_valid():
            bs.save()  # 生成记录
            return Response(bs.data)
        else:
            return Response(bs.errors)

class PublishDetailView(APIView):
    def get(self,request,pk):
        publish_obj=models.Publish.objects.filter(pk=pk).first()
        bs=PublishSerializers(publish_obj,many=False)
        return Response(bs.data)
    def put(self,request,pk):
        publish_obj = models.Publish.objects.filter(pk=pk).first()

        bs=PublishSerializers(data=request.data,instance=publish_obj)
        if bs.is_valid():
            bs.save() # update
            return Response(bs.data)
        else:
            return Response(bs.errors)
    def delete(self,request,pk):
        models.Publish.objects.filter(pk=pk).delete()

        return Response("")
```



## 2.mixin类和generics编写视图



```python
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
class PublishView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset=models.Publish.objects.all()
    serializer_class=PublishSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class PublishDetailView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset=models.Publish.objects.all()
    serializer_class=PublishSerializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
```



## 3.使用generics 下ListCreateAPIView,RetrieveUpdateDestroyAPIView



```
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
class PublishView(ListCreateAPIView):
    queryset=models.Publish.objects.all()
    serializer_class=PublishSerializers

class PublishDetailView(RetrieveUpdateDestroyAPIView):
    queryset=models.Publish.objects.all()
    serializer_class=PublishSerializers
```



## 4.使用ModelViewSet

路由：

```python
url(r'^publish/$', views.PublishView.as_view({'get':'list','post':'create'})),
    url(r'^publish/(?P<pk>\d+)/$', views.PublishView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
```

视图：

```
from rest_framework.viewsets import ModelViewSet
class PublishView(ModelViewSet):
    queryset=models.Publish.objects.all()
    serializer_class=PublishSerializers
```

 

# 二、ViewSetMixin

-ViewSetMixin

```python

# ViewSetMixin 写在前面,先找ViewSetMixin的as_view方法
# 用了ViewSetMixin ,视图类中,不需要再写get,post,delete....这些函数了,函数名可以自定义
# 而且这个视图类,可以响应多条路由
        
-使用:
	-urls.py中
      url(r'^publishs/', views.PublishView.as_view({'get': 'aaa','post':'ddd'})),
      url(r'^bbb/', views.PublishView.as_view({'get': 'bbb','post':'ccc'})),
                
    -视图类中:
       class PublishView(ViewSetMixin,APIView):
          def aaa(self,request):
               return Response({'status':100})
          def bbb(self,request):
               return Response({'bb': "bbb"})
```



# 三、路由控制器

## 　　1.自定义路由（原生方式）

```
from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^books/$', views.BookView.as_view()),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view()),
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
class BookView(APIView):

    def get(self, request):
        book_list = models.Book.objects.all()
        bs = BookSerializers(book_list, many=True)
        return Response(bs.data)

    def post(self, request):
        # 添加一条数据
        print(request.data)

        bs=BookSerializers(data=request.data)
        if bs.is_valid():
            bs.save()  # 生成记录
            return Response(bs.data)
        else:

            return Response(bs.errors)

class BookDetailView(APIView):
    def get(self,request,pk):
        book_obj=models.Book.objects.filter(pk=pk).first()
        bs=BookSerializers(book_obj,many=False)
        return Response(bs.data)
    def put(self,request,pk):
        book_obj = models.Book.objects.filter(pk=pk).first()

        bs=BookSerializers(data=request.data,instance=book_obj)
        if bs.is_valid():
            bs.save() # update
            return Response(bs.data)
        else:
            return Response(bs.errors)
    def delete(self,request,pk):
        models.Book.objects.filter(pk=pk).delete()

        return Response(""
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

## 　　2.半自动路由（视图类继承ModeViewSet）

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^publish/$', views.PublishView.as_view({'get':'list','post':'create'})),
    url(r'^publish/(?P<pk>\d+)/$', views.PublishView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from rest_framework.viewsets import ModelViewSet
class PublishView(ModelViewSet):
    queryset=models.Publish.objects.all()
    serializer_class=PublishSerializers
```

 

## 　　3.全自动路由（自动生成路由）

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from django.conf.urls import url,include
from app01 import views
from rest_framework import routers
router=routers.DefaultRouter()
# 两个参数，一个是匹配的路由，一个是视图中写的CBV的类
router.register('publish',views.PublishView)
urlpatterns = [
    # http://127.0.0.1:8000/publish/format=json(渲染器通过这个判断，返回渲染的页面)
    # url(r'^publish/', views.PublishView.as_view({'get':'list','post':'create'})),
    # http://127.0.0.1:8000/publish.json(渲染器通过这个判断，返回渲染的页面)
    # url(r'^publish\.(?P<format>\w+)$', views.PublishView.as_view({'get':'list','post':'create'})),
    
    # 可以用 以下方式访问
    # 1 http://127.0.0.1:8000/publish/
    # 2 http://127.0.0.1:8000/publish.json
    # 3 http://127.0.0.1:8000/publish/3
    # 4 http://127.0.0.1:8000/publish/3.json   
    url(r'',include(router.urls))
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from rest_framework.viewsets import ModelViewSet
class PublishView(ModelViewSet):
    queryset=models.Publish.objects.all()
    serializer_class=PublishSerializers
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
# 小结：
-传统的url配置
   url(r'^books/$', views.BookView.as_view()),
   url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view()),
  -半自动
    url(r'^publish/$', views.PublishView.as_view({'get':'list','post':'create'})),
   url(r'^publish/(?P<pk>\d+)/$', views.PublishView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
  -全自动(了解)
   -能自动生成多条路由
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

# 四、解析器

　　1.解析器的作用

　　　　根据请求头content-type选择对应的解析器队请求体内容进行处理

　　　　有appliction/json,x-www-form-urlencoded，form-data等格式

　　2.全局使用解析器

　　　　setting里

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES':[
        'rest_framework.parsers.JSONParser'
        'rest_framework.parsers.FormParser'
        'rest_framework.parsers.MultiPartParser'
    ]

}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

　　　　路由：

```
urlpatterns = [
    url(r'test/', TestView.as_view()),
]
```

　　　　视图函数：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.content_type)

        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

## 　　3.局部使用解析器

a.仅处理请求头content-type为appliction/json请求体

```
from django.conf.urls import url, include
from web.views.s5_parser import TestView

urlpatterns = [
    url(r'test/', TestView.as_view(), name='test'),
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import JSONParser


class TestView(APIView):
    parser_classes = [JSONParser, ]

    def post(self, request, *args, **kwargs):
        print(request.content_type)

        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)

        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)

        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

b.仅处理请求头content-type为appliction/x-www-from-urlencoded的请求体

```
from django.conf.urls import url, include
from web.views import TestView

urlpatterns = [
    url(r'test/', TestView.as_view(), name='test'),
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import FormParser


class TestView(APIView):
    parser_classes = [FormParser, ]

    def post(self, request, *args, **kwargs):
        print(request.content_type)

        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)

        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)

        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

c.仅仅处理请求头content-type为multipart/form-data的请求体

```
from django.conf.urls import url, include
from web.views import TestView

urlpatterns = [
    url(r'test/', TestView.as_view(), name='test'),
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import MultiPartParser


class TestView(APIView):
    parser_classes = [MultiPartParser, ]

    def post(self, request, *args, **kwargs):
        print(request.content_type)

        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="http://127.0.0.1:8000/test/" method="post" enctype="multipart/form-data">
    <input type="text" name="user" />
    <input type="file" name="img">

    <input type="submit" value="提交">

</form>
</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

d.仅上传文件

```
from django.conf.urls import url, include
from web.views import TestView

urlpatterns = [
    url(r'test/(?P<filename>[^/]+)', TestView.as_view(), name='test'),
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import FileUploadParser


class TestView(APIView):
    parser_classes = [FileUploadParser, ]

    def post(self, request, filename, *args, **kwargs):
        print(filename)
        print(request.content_type)

        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="http://127.0.0.1:8000/test/f1.numbers" method="post" enctype="multipart/form-data">
    <input type="text" name="user" />
    <input type="file" name="img">

    <input type="submit" value="提交">

</form>
</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

e.同时多个Parser

当同时使用多个parser时，rest_framework会根据请求头content-type自动进行比对，并使用对应parser

```
from django.conf.urls import url, include
from web.views import TestView

urlpatterns = [
    url(r'test/', TestView.as_view(), name='test'),
]
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


class TestView(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser, ]

    def post(self, request, *args, **kwargs):
        print(request.content_type)

        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

## 　　4.源码分析

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
1 在调用request.data时，才进行解析，由此入手
    @property
    def data(self):
        if not _hasattr(self, '_full_data'):
            self._load_data_and_files()
        return self._full_data
        
2 查看self._load_data_and_files()方法---->self._data, self._files = self._parse()

        def _parse(self):
            #用户请求头里content_type的值
            media_type = self.content_type

            #self.parsers 就是用户配置的parser_classes = [FileUploadParser,FormParser ]
            #self里就有content_type，传入此函数
            parser = self.negotiator.select_parser(self, self.parsers)

3 查看self.negotiator.select_parser(self, self.parsers)
     def select_parser(self, request, parsers):
        #同过media_type和request.content_type比较，来返回解析器，然后调用解析器的解析方法
        #每个解析器都有media_type = 'multipart/form-data'属性
        for parser in parsers:
            if media_type_matches(parser.media_type, request.content_type):
                return parser
        return None
    
4 最终调用parser的解析方法来解析parsed = parser.parse(stream, media_type, self.parser_context)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
1 Request实例化，parsers=self.get_parsers()
    Request(
                request,
                parsers=self.get_parsers(),
                authenticators=self.get_authenticators(),
                negotiator=self.get_content_negotiator(),
                parser_context=parser_context
            )
2 get_parsers方法，循环实例化出self.parser_classes中类对象
    def get_parsers(self):
        return [parser() for parser in self.parser_classes]            

3 self.parser_classes 先从类本身找，找不到去父类找即APIVIew 中的
    parser_classes = api_settings.DEFAULT_PARSER_CLASSES
4 api_settings是一个对象，对象里找DEFAULT_PARSER_CLASSES属性，找不到，会到getattr方法
        def __getattr__(self, attr):
            if attr not in self.defaults:
                raise AttributeError("Invalid API setting: '%s'" % attr)

            try:
                #调用self.user_settings方法，返回一个字典，字典再取attr属性
                val = self.user_settings[attr]
            except KeyError:
                # Fall back to defaults
                val = self.defaults[attr]

            # Coerce import strings into classes
            if attr in self.import_strings:
                val = perform_import(val, attr)

            # Cache the result
            self._cached_attrs.add(attr)
            setattr(self, attr, val)
            return val
 5 user_settings方法 ，通过反射去setting配置文件里找REST_FRAMEWORK属性，找不到，返回空字典
    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'REST_FRAMEWORK', {})
        return self._user_settings
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

# 五、响应器

## 　　1.作用

　　　　根据用户请求url或用户可接受的类型，筛选出合适的渲染组件

　　　　用户请求URL：

　　　　　　http://127.0.0.1:8000/test/?format=json
  　　　   http://127.0.0.1:8000/test.json

　　

## 　　2.内置渲染器　　

**显示json格式：JSONRenderer**

访问URL：

- http://127.0.0.1:8000/test/?format=json

- http://127.0.0.1:8000/test.json

- http://127.0.0.1:8000/test/

   

**默认显示格式：BrowsableAPIRenderer（可以修改它的html文件）**

访问URL：

- http://127.0.0.1:8000/test/?format=api
- http://127.0.0.1:8000/test.api
- http://127.0.0.1:8000/test/

 

**表格方式：AdminRenderer**

访问URL：

- http://127.0.0.1:8000/test/?format=admin
- http://127.0.0.1:8000/test.admin
- http://127.0.0.1:8000/test/

 

**form表单方式：HTMLFormRenderer**

访问URL：

- http://127.0.0.1:8000/test/?format=form
- http://127.0.0.1:8000/test.form
- http://127.0.0.1:8000/test/

## 　　3.局部使用

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from rest_framework.renderers import  HTMLFormRenderer,BrowsableAPIRenderer
class BookDetailView(APIView):
    renderer_classes = [HTMLFormRenderer,BrowsableAPIRenderer ]
    def get(self,request,pk):
        book_obj=models.Book.objects.filter(pk=pk).first()
        bs=BookSerializers(book_obj,many=False)
        return Response(bs.data)
    def put(self,request,pk):
        book_obj = models.Book.objects.filter(pk=pk).first()

        bs=BookSerializers(data=request.data,instance=book_obj)
        if bs.is_valid():
            bs.save() # update
            return Response(bs.data)
        else:
            return Response(bs.errors)
    def delete(self,request,pk):
        models.Book.objects.filter(pk=pk).delete()

        return Response("")
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

## 　　4.全局使用

　　　　setting里配置：

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':['rest_framework.renderers.JSONRenderer']
}
```

 

## 　　5.自定义显示模板

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from rest_framework.renderers import  TemplateHTMLRenderer
class BookDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self,request,pk):
        book_obj=models.Book.objects.filter(pk=pk).first()
        bs=BookSerializers(book_obj,many=False)
        return Response(bs.data,template_name='aa.html')
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{{ title }}
{{ publishDate }}
</body>
</html>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)