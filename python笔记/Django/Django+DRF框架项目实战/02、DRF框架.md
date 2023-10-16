## DRF框架

# 一、开发模式和RESTful

## 1、web应用开发模式

## 2、REESTful介绍

### 	2.1 RESTFul特点：

​		1、每个URI代表1中子源

​		2、客户端使用GET、POST、PUT、DELETE 4个标识操作方式的动词对服务器资源进行操作

- GET 用来获取资源	
- POST 用来新建资源
- PUT 用来更新资源（整体更新）
- PATCH 用来更新资源（局部更新）
- DELETE 用来删除资源


3、通过操作医院的表现形式来操作资源

4、资源的形式是XML或者JSON

5、客户端与服务器之间的交互在请求之间是无状态的，从客户端到服务端的每个请求都必须包含理解请求所必需的信息。

## 3、RESTful API设计风格

### 1、HTTP动词

### 2、url路径

- 路径尽量用名词表示，而不用动词
  - 推荐
    - http://aip.baidu.com/projects
    - http://api.baidu.com/envs
- 不管是单一资源还是所有资源，路径中名词尽量用复数



### 3、过滤参数

### 4、返回状态码



### 5、返回内容



# 二、DRF框架介绍

## 1、安装和使用

```python
pip install djangorestframework
```

注册到项目中

## 2、Django开发RESTful接口

- 1、定义模型类
- 2、定义路由
- 3、定义视图

## 3、DRF开发RESTful接口

- 1、定义模型类
- 2、定义序列化器
  - 作用：
    - 进行序列化操作，将ORM对象转换为json数据
    - 进行反序列化，将json转换为ORM对象
      - 进行反序列化操作的时候，会对json数据中的每个字段进行校验
- 3、定义路由
- 4、定义视图

# 三、序列化器

## 1、序列化器的定义

​	Django REST framework中的序列化器通过类来定义，必须继承自rest_framework.serializers.Serializer。

序列化器中的字段和模型类中的字段类型保持一致。

模型类如下：

```python
class UserInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')
    pwd = models.CharField(max_length=18, verbose_name='密码')
    email = models.EmailField(max_length=40, verbose_name='邮箱')
    age = models.IntegerField(verbose_name='年龄', default=18)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "userinfo"
        verbose_name = '用户信息'

```



序列化器的定义：

```python

class UserInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=18)
    pwd = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=40)
    age = serializers.IntegerField(min_value=0, max_value=150)

    def create(self, validated_data):
        """
        自定义一个序列化器保存数据的方法
        :param validated_data:
        :return:
        """
        UserInfo.objects.create(validated_data)
        return validated_data

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.pwd = validated_data['pwd']
        instance.email = validated_data['email']
        instance.age = validated_data['age']

        instance.save()
        return instance
```



## 2、字段类型与选项介绍

## 3、序列化操作

##### 1、环境准备

1、安装

###### 	2、创建应用

###### 	3、修改setting中的配置

###### 	4、model.py中定义模型类

```python
class UerInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')
    pwd = models.CharField(max_length=18, verbose_name='密码')
    email = models.EmailField(max_length=40, verbose_name='邮箱')
    age = models.IntegerField(verbose_name='年龄', default=18)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "userinfo"
        verbose_name = '用户信息'
```

###### 	5、定义序列化器	

- 在应用中新建文件serializer.py

- 在文件serializer.py中定义序列化器

  ```python
  
  from rest_framework import serializers
  
  
  class UserInfoSerializer(serializers.Serializer):
      name = serializers.CharField(max_length=18)
      pwd = serializers.CharField(max_length=20)
      email = serializers.EmailField(max_length=40)
      age = serializers.IntegerField(min_value=0, max_value=150)
  
  ```

  ###### 6、激活迁移文件

  ###### 7、练习数据准备

  ```python
  # 进入交互环境添加测试数据
  UserInfo.objects.create(name='张三',pwd='123435',email='1234@qq.com',age=10)
  UserInfo.objects.create(name='李四',pwd='123435',email='1234@qq.com',age=10)
  UserInfo.objects.create(name='王五',pwd='123435',email='1234@qq.com',age=10)
  ```

  

##### 2、序列化操作

- 序列化：将python对象--->转化为json格式的数据

  定义好Serializer类后，如果要通过序列化器类进行序列化，需要先创建Serializer对象。

  Serializer参数为：

  ```python
  Serializer(instance=None,data={empty},**kwargs)
  ```

  1)用于序列化时，将模型对象传入instance参数

  2)用户反序列化时，将要被反序列化的数据传入data参数

  1、单个数据序列化

  ```python
  # 通过模型类查询一条用户信息
  obj = UserInfo.objects.first()
  # 使用查询到的用户信息，创建一个序列化对象
  ser = UserInfoSerializer(obj)
  # 
  ser.data
  {'name': '张三', 'pwd': '123435', 'email': '1234@qq.com', 'age': 10}
  
  ```

  2、查询集序列化

  ```python
  obj = UserInfo.objects.all()
  ser = UserInfoSerializer(obj,many=True)
  ser.data
  [OrderedDict([('name', '张三'), ('pwd', '123435'), ('email', '1234@qq.com'), ('age', 10)]), OrderedDict([('name', '李四'), ('pwd', '123435'), ('email', '1234@qq.com'), ('age', 10)]), OrderedDict([('name', '王五'), ('pwd', '123435'), ('email', '1234@qq.com'), ('age', 10)])]
  
  ```

  - 对多个数据进行序列化加参数：many=True

  3、将序列化的数据转换为json
  
  ```python
  
  from rest_framework.renderers import JSONRenderer
  # 查询用户是对象
  obj = UserInfo.objects.get(id=1)
  # 创建序列化器对象
  u = UserInfoSerializer(obj)
  # 将得到的字段，转换为json数据
  JSONRenerer().render(u.data)
  ```

##### 3、关联对象嵌套序列化

1、数据准备

​	定义模型类：

```python

class Addr(models.Model):
    user = models.ForeignKey("UserInfo",verbose_name='所属用户',on_delete=models.CASCADE)
    mobile = models.CharField(verbose_name='手机号',max_length=19)
    city = models.CharField(verbose_name='城市',max_length=20)
    info = models.CharField(verbose_name="详细地址",max_length=200)

    def __str__(self):
        return self.info
```

插入数据

```python
obj = UserInfo.objects.get(id=1)
Addr.objects.create(user=obj,mobile='18898789878',city='长沙',info='湖南长沙市阅览区')
<Addr: 湖南长沙市阅览区>
Addr.objects.create(user=obj,mobile='188987823278',city='长沙',info='湖南长沙撒旦发生发')
<Addr: 湖南长沙撒旦发生发>
```

查询：

```python
UserInfo.objects.get(id=1).addr_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x000001C95FCB4C40>

```



定义序列化器类

```python
class AddrSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=18)
    city = serializers.CharField(max_length=20)
    info = serializers.CharField(max_length=200)

    # 关联字段序列化
    user = serializers.PrimaryKeyRelatedField()
```

2、关联字段序列化的方式

- 1、PrimaryKeyRelatedField

- 返回关联字段的id

- ```python
  user = serializers.PrimaryKeyRelatedField()
  
  ```

  2、StringRelatedFiled

  - 返回关联字段模型类__str__方法返回的内容

  - ```python
    
    user = serializers.StringRelatedField()
    ```

  3、使用关联对象的序列化器

  - 返回关联对象序列化器返回的所有字段

  - ```python
    # 关联模型的序列化器
    user = UserInfoSeralizer()
    ```

- 4、SlugRelatedField

- 指定返回关联对象某个具体字段

- ```python
  user = seralizers.SlugRelatedField(read_only=True,slug_field = 'name')
  ```

- 

## 4、反序列化操作

- 反序列化----->将json格式数据 转换为python对象

在进行反序列化操作时，会对对象数据进行验证，验证通过的情况下再进行保存

反序列化时，初始化序列化器对象，将要被反序列化的数据传入data参数

##### 1、数据验证

- a）校验数据
  - 调用is_valid()方法进行校验，验证成功后返回True，否则返回False

##### 2、常用校验字段说明



3、将序列化得到的数据转换为json

```python
from rest_framework.renderers import JSONRenderer
# 查询用户对象
obj = UserInfo.objects.get(id=1)
# 创建序列化对象
u = UserInfoSerializer(obj)
# 将得到的字段，转为json数据
JSONRenderer().render(u.data)
```

##### 3、序列化器保存数据

验证通过后，如需保存数据，直接调用序列化器对象的save方式即可，save方法会自动触发序列化器中对应的方法来保存数据

```python
#反序列化
ser = UserInfoSerializer(data=data)
#校验数据
ser.is_valid()
# 保存数据
ser.save()
```

注意点：

- 保存：save会调用序列化器中定义的create方法
- 更新：save会调用序列化器中的定义的update方法

## 5、模型序列化器

为了方便我们定义序列化器，DRF为我们提供了ModelSerializer模型类序列化器来帮助我们快速创建一个Serializer类。

ModelSerializer与常规的Serializer相同，但提供了：

- 基于模型类自动生成一些列字段
- 基于模型类自动为Serializer生成validators ，比如unique_together
- 包含默认的create()和update()的实现

##### 1、模型序列化器的使用

- 定义模型化序列化器类，直接继承于serializers.ModelSerializer即可

  ```python
  class UserInfoSerializer(serializers.ModelSerializer):
      class Meta:
         model = UserInfo
         fields = "__all__"
  ```
  
  -指定模型类和需要序列化的字段
  
  - model指明参照哪个模型类
  - fields指明模型类的哪些字段生成

##### 2、指定字段

1、fields

- fields =“__all__" 代表模型类中所有字段都进行序列化

2、exclude 使用exclude可以明确排除哪些字段不参与序列化

3、read_only_fields 指明只读的字段（只参与序列化，不参与反序列化)

##### 3、修改字段的参数选项

- 使用extra_kwargs 参数为ModelSerializer添加或者修改原有的选项参数 反序列化校验规则 

  - 通过字段名指定字段对应的参数和值

  - ```python
    class UserInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = UserInfo
            fields = "__all__"
            extra_kwargs = {
                'pwd': {'min_value': 0,
                        'required': True},
            }
    
    ```

    

## 6、序列化器保存数据案例

- 前提是序列化模型类要是实现create方法和update方法

- 使用序列化器新增数据：

- ```python
  user1 = {'id': 1, 'name': 'sunliguo', 'pwd': '123435', 'email': '1234@qq.com', 'age': 10}
  ser = UserInfoSerializer(data=user1)
  # 校验数据
  ser.is_valid()
  # 保存数据
  ser.save()
  ```

使用序列化器修改数据：

```python
user = UserInfo.objects.get(id=1)
user1 = {'id': 1, 'name': 'sunliguo', 'pwd': '123435', 'email': '1234@qq.com', 'age': 10}
#创建序列化器
ser = UserInfoSerializer(instance=user,data=user1)
# 校验数据
ser.is_valid()
# 保存数据
ser.save()
```



## 7、利用序列化器实现增删改查的接口

视图

```python

def user_list(request):
    """
    get方法请求：获取用户列表
    post方法请求：添加用户信息
    :param request:
    :return:
    """
    if request.method == "GET":
        # 获取用户信息列表
        users = UserInfo.objects.all()
        # 创建序列化对象
        ser = UserInfoSerializer(users, many=True)
        result = {
            'data': ser.data,
            'code': 200,
            "message": "OK"
        }
        return JsonResponse(result)
    elif request.method == 'POST':
        params = JSONParser().parse(request)
        # 创建序列化器
        ser = UserInfoSerializer(data=params)
        # 校验请求数据
        if ser.is_valid():
            # 校验通过，则添加数据到数据
            ser.save()
            return JsonResponse({'code': 201, 'data': ser.data, "message": 'OK'})
        else:
            return JsonResponse({'code': 400, 'message': ser.errors})

    else:
        return JsonResponse({'code': 405, 'message': f"不支持该请求{request.method}"})


def user_detail(request, id):
    """
    GET:获取单个用户信息
    PUT：修改单个用户信息
    DELETE:删除用户信息
    :param request:
    :param id:
    :return:
    """
    try:
        obj = UserInfo.objects.get(id=id)
    except Exception as e:
        return HttpResponse('404 访问资源不存在', status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser = UserInfoSerializer(obj)
        return JsonResponse({'code': 200, "data": ser.data, 'message': "OK"})
    elif request.method == "PUT":
        # 修改单个用户资源

        # ser = UserInfoSerializer(instance=obj, data=json.loads(request.body.decode('utf-8')))

        params = JSONParser().parse(request)
        ser = UserInfoSerializer(instance=obj, data=params)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'code': 200, "data": ser.validated_data, "message": "OK"})
        else:
            return JsonResponse({'code': 400, 'message': ser.errors})
    elif request.method == 'DELETE':
        obj.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'code': 405, 'message': f"不支持该请求{request.method}"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

```

路由：

```python
   path('users/', views.user_list),
    re_path(r'users/(.+?)/', views.user_detail),
```



## 8、自定义验证方法

DRF支持自定义序列化器的校验方法：

- 定义校验方法

  - 验证方法名的规范：validate_字段名

    ```python
    class UserInfoSerializer(serializers.Serializer):
        def validate_pwd(self,value):
            """校验逻辑"""
    ```

- 通过validators字段指定验证函数



```python
  def leng_validate(value):
      if not(10<len(value)<20):
          raise serializers.ValidationError('字段的长度不在10-20之间')
       
  class UserInfoSerializer(serializers.Serializer):
      pwd = serializers.CharField(validators=length_validate)
      
        
```



# 三、请求和响应对象

## 1、DRF定义视图函数

案例：
```

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

@api_view(['GET','POST'])
def user_list(request):
    return Response(data={'message':"OK"})

# Django 的request获取请求参数

# request.GET	#获取get请求传递的查询参数
# request.POST   #获取post请求传递的表单参数

# put patch post请求传递到请求体参数（json格式），Django中没有提供直接获取的方法
params = request.body.decode()
import json
params = json.loads(params)

DEF中的request对象：
1、对应查询参数（拼接在url后面的参数）的获取：
	request.query_params
 2、表单参数、json
	request.data

```

## 2、DRF的Request对象

REST framework传入视图的request对象不再是Django默认的HttpRequest对象，而是REST framework提供的扩展了HttpRequest类的Request类的对象。无论前端发送的哪种格式的数据，我们都可以以统一的方式读取数据。

​	1、request.data属性

## 3、DRF的Response对象

## 4、响应状态码

## 5、API视图的装饰器

REST框架提供了两个可用于编写API视图的装饰器

- 用于处理基于函数的装饰器  @api_view

```
Decorator that converts a function-based view into an APIView subclass.Takes a list of allowed methods for the view as an argument.
将基于函数的视图转换为 APIView 子类的装饰器。将视图允许的方法列表作为参数。

```



- 用于处理基于类的视图的类 。APIView

下面我们通过@api_view这个装饰器来实现增删改查接口

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.

class UserListView(APIView):
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass


@api_view(['GET', 'POST'])
def user_list(request):
    """
    get方法请求：获取用户列表
    post方法请求：添加用户信息
    :param request:
    :return:
    """
    if request.method == "GET":
        # 获取用户信息列表
        users = UserInfo.objects.all()
        # 创建序列化对象
        ser = UserInfoSerializer(users, many=True)
        result = {
            'data': ser.data,
            'code': 200,
            "message": "OK"
        }
        return Response(result, status=status.HTTP_200_OK)
    elif request.method == 'POST':

        # 创建序列化器
        ser = UserInfoSerializer(data=request.data)
        # 校验请求数据
        if ser.is_valid():
            # 校验通过，则添加数据到数据
            ser.save()
            return Response({'code': 201, 'data': ser.data, "message": 'OK'})
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):
    """
    GET:获取单个用户信息
    PUT：修改单个用户信息
    DELETE:删除用户信息
    :param request:
    :param id: 操作资源的id
    :return:
    """
    try:
        obj = UserInfo.objects.get(id=id)
    except Exception as e:
        return Response({"code": 404, "message": "404,访问的资源不存在!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = UserInfoSerializer(obj)
        return Response({'code': 200, "data": ser.data, 'message': "OK"}, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        # 修改单个用户资源
        # ser = UserInfoSerializer(instance=obj, data=json.loads(request.body.decode('utf-8')))

        ser = UserInfoSerializer(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'code': 200, "data": ser.validated_data, "message": "OK"}, status=status.HTTP_200_OK)
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)



```

## 6、使用DRF给url添加后缀

1、修改视图函数

在视图函数后面添加参数format，并设置默认值为空

```python
@api_view(['GET','POST'])
def user_list(request,format=None):
    pass
@api_view(['GET','PUT','DELETE'])
def user_detail(request,id,format=None):
    pass
```

2、修改路由配置

```python
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('users/',views.user_list),
    path('users/<int:id>/',view.user_detail)
]
urlpatterns = format_suffix_patterns(urlpatterns)
```

3、效果

```python

# 访问： Http://127.0.0.1:8000/app1/user.json 返回json数据
# 访问 http://127.0.0.1:8000/app1/users.api 访问DRF自带的接口调试页面
```

## 7、类视图APIView

1、APIView与View的区别：

- 传入到视图方法中的是REST framework的Request对象
- 视图方法可以返回REST framework的Response对象
- 任何APIException异常都会被捕获到，并且处理成合适的响应信息。
- 扩展了身份认证、权限检查、流量控制这个三个功能

2、扩展的功能

- authentication_classes:身份认证
- permission classes ：权限检查
- throttle_classes:限流

3、基于APIView实现增删查改



# 四、视图集和路由

## 1、GenericAPIView

rest_framework.generics.GenericAPIView继承自APIView，增加了对于列表视图的详情视图可能用到的通用支持方法。

1、扩展的类属性

- queryset :指定当前视图使用的查询集
- serializer_class:类视图使用的序列化器

2、扩展的方法：

- self.queryset():获取查询集
- self.serializer():获取序列化器
- self.get_object():获取指定的单一对象

3、扩展功能

- pagination_clas:数据分页
- filter_backends:数据过滤&排序
- 指定单一数据获取的参数字段：
  - lookup_field 查询单一数据库对象时使用的条件字段，默认为‘pk’
  - lookup_url_kwarg 查询单一数据时URL中的参数关键字名称，默认与lookup_field相同

## 2、扩展视图类

### 1、基本扩展类：

- ListModelMinxin:
  - 列表视图扩展类，提供'list'方法快速实现列表视图
  - 状态码：200
- CreateModelMixin：
  - 创建视图扩展类，提供create方法快速实现创建资源的视图
  - 成功返回201状态码，如果序列化器对前端发送的数据验证失败，返回400错误。
- RetrieveModelMixin：获取单一数据
  - 详情视图扩展类，提供retrieve方法，可以快速实现返回一个存在的数据对象。
  - 如果成功，返回200，否则返回404
- UpdateModelMixin：更新数据
  - 更新视图扩展类，提供update方法和partial_update方法，可以快速实现更新一个存在的数据对象。
  - 成功返回200，序列化器校验数据失败时，返回400错误。
- DestroyModelMixin：
  - 删除视图扩展类，提供destroy方法，可以快速实现删除一个存在的数据对象。
  - 成功返回204，不存在返回404。

### 2、视图扩展类

1、CreateAPIView

- 继承自：GenericAPIView、CreateModelMixin
- 提供post方法

2、ListAPIView

- 继承自GenericAPIView、ListModelMixin
- 提供get方法

3、RetireveAPIView

- 继承自：GenericAPIView，RetrieveModelMixin
- 提供get方法

4、DestoryAPIView

- 继承自：GenericAPIView、DestoryModelMixin
- 提供delete方法

5、UpdateAPIView

- 继承自：GenericAPIView、UpdateModelMixin
- 提供put和patch方法

## 3、视图集

1、视图集的使用

ViewSet视图集类不再实现get()、post()等方法，而是实现action如list()、create()等。将一系列逻辑相关的动作放到一个类中：

- list()提供一组数据
- retrieve()提供单个数据
- create()创建数据
- update()保存数据
- destory()删除数据

注意点：

在使用视图集的时候，在配置路由的时候，用自行指定请求方法和处理的视图函数。

```
urlpatterns = [
path(r'^books/$',xxViewSet.as_view({'get':list})),
path(r'^books/<int:id>/$',xxxInfoViewSet.as_view({'get':'retrieve'}))
]
```

2、action属性

视图集只在使用as_view()方法的时候，才会将action动作与具体请求方式对应上。

3、常用视图集类

1）ViewSet

继承自APIView，作用也与APIView基本雷士，提供了身份认证、权限校验、流量管理等。

在ViewSet中，没有提供任何动作action方法，需要我们自己实现action方法

2）GenericViewSet

继承自GenericAPIView，作用也与GenericAPIView类似，提供了get_object、get_queryset等方法便于列表视图与详情信息视图的开发。

3）ModelViewSet

继承自GenericAPIView，同时包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMinxin、DestoryModelMinxin。

4）ReadOnlyModelViewSet

继承自GenericAPIView，同时包括了ListModelMixin、RetrieveModelMixin。

4、路由

对于视图集ViewSet，我们除了可以自己手动指明请求方式与动作action之间的对应关系外，还可以使用

# 五、其他功能

#### 1、认证&权限

#### 2、限流

#### 3、过滤

对于列表数据可能需要根据字段进行过滤，我们可以通过田间django-filter扩展来增强支持

```python
pip install django-filter
```

在配置文件中增加过滤后端的设置：

```python
# 注册到应用
INSTALLED_APPS = [
   ...
    'django_filters',

]

# 配置DRF过滤器
REST_FRAMEWORK = {

    # 配置DRF过滤器
    'DEFAULT_FILTER_BACKENDS':['django_filters.rest_framework.DjangoFilterBackend']
}
```

在视图中添加filterset_fields属性，指定可以过滤的字段

```python
class StudentView(ListAPIView):
	queryset = BookInfo.objects.all()
	serializer_class = BookInfoSerializer
	filterset_fields = ('age',)
```



#### 4、排序

#### 5、分页

#### 6、异常处理

#### 7、文件上传

#### 8、接口文档



# 六、ajax跨域

# 七、DRF JWT

### 1、token鉴权和JWT介绍

### 2、simpleJWT

1、安装djangorestframework-simplejwt

```python
pip install djangorestframework-simplejwt
```

2、settings.py中添加配置

- 注册到应用中

```
INSTALLED_APPS = [
   ...
    'rest_framework_simplejwt',
]
```

- DRF配置鉴权方式

  ```python
  # DRF的配置鉴权方式
  REST_FRAMEWORK = {
      # 配置登录鉴权方式
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework_simplejwt.authentication.JWTAuthentication',
          'rest_framework.authentication.SessionAuthentication',
          'rest_framework.authentication.BasicAuthentication',
      )
  }
  ```

3、路由中添加登录认证的配置

```
urlpatterns = [
    path('login/', TokenObtainPairView.as_view())
]

```



### 3、登录接口开发