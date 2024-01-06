### DRF实现增删改查：

### 1、前提准备：模型类和序列化器

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



```python
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
        # extra_kwargs = {
        #     'pwd': {'min_value': 0,
        #             'required': True},
        # }

    def validate_pwd(self, value):
        """自定义的字段校验器"""
        if not 6 < len(value) < 18:
            raise serializers.ValidationError('pwd长度需要在10-18之间')
        return value
```

处理逻辑：

序列化：Queryset ->ModelSerializer->ser.data

反序列化：json->ModelSerializer>ser.is_valid()->ser.save()



#### 1、基于视图函数的实现

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
            return JsonResponse({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return JsonResponse({'code': 405, 'message': f"不支持该请求{request.method}"})


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
        return HttpResponse('404 访问资源不存在', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = UserInfoSerializer(obj)
        return JsonResponse({'code': 200, "data": ser.data, 'message': "OK"})
    elif request.method == "PUT":
        # 修改单个用户资源
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

#### 2、api_view装饰器将基于函数的视图转化为APIView的子类

提供的功能：

1、request.data 直接获取前端提供的数据

2、只提供允许的请求方法

```python

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

#### 3、基于APIView

1、直接写get，post等请求方法同名的函数

```python

class UserListView(APIView):
    def get(self, request, format=None):
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

    def post(self, request, format=None):
        # 创建序列化器
        print(request.data)
        ser = UserInfoSerializer(data=request.data)
        # 校验请求数据
        if ser.is_valid():
            # 校验通过，则添加数据到数据
            ser.save()
            return Response({'code': 201, 'data': ser.data, "message": 'OK'})
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get_object(self, id):
        try:
            return UserInfo.objects.get(id=id)
        except Exception as e:
            raise Http404()

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        ser = UserInfoSerializer(obj)
        return Response({'code': 200, "data": ser.data, 'message': "OK"}, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        obj = self.get_object(id)
        # 修改单个用户资源
        ser = UserInfoSerializer(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'code': 200, "data": ser.validated_data, "message": "OK"}, status=status.HTTP_200_OK)
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        obj = self.get_object(id)
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

```

#### 4、将模型类和模型序列化器提取处来，换个别的模型类和序列化器同样适用



```python
class UserListView(APIView):
    # 设置模型类
    model = UserInfo
    # 设置序列化类
    serializer = UserInfoSerializer

    def get(self, request, format=None):
        # 获取用户信息列表
        users = self.model.objects.all()
        # 创建序列化对象
        ser = self.serializer(users, many=True)
        result = {
            'data': ser.data,
            'code': 200,
            "message": "OK"
        }
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # 创建序列化器
        ser = self.serializer(data=request.data)
        # 校验请求数据
        if ser.is_valid():
            # 校验通过，则添加数据到数据
            ser.save()
            return Response({'code': 201, 'data': ser.data, "message": 'OK'})
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    # 设置模型类
    model = UserInfo
    # 设置序列化类
    serializer = UserInfoSerializer

    def get_object(self, id):
        try:
            return self.model.objects.get(id=id)
        except Exception as e:
            raise Http404()

    def get(self, request, id, format=None):
        obj = self.get_object(id)
        ser = self.serializer(obj)
        return Response({'code': 200, "data": ser.data, 'message': "OK"}, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        obj = self.get_object(id)
        # 修改单个用户资源
        ser = self.serializer(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'code': 200, "data": ser.validated_data, "message": "OK"}, status=status.HTTP_200_OK)
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        obj = self.get_object(id)
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

```

#### 	5、GenericAPIView(views.APIView)的再次封装

需要设置的属性：

- queryset =None      指定当前类视图使用的查询集
- serializer_class = None   类视图使用的序列化器

其他属性：

- lookup_field = 'pk'
- lookup_url_kwarg = None

提供的方法：

- get_queryset()   获取查询集
- get_object() 获取指定的单一对象
- get_serializer()   获取序列化器
- get_serializer_class()

```python
class UserListView(GenericAPIView):
    # 设置模型类
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def get(self, request, format=None):
        # 获取用户信息列表
        users = self.get_queryset()
        # 创建序列化对象
        # ser = self.serializer_class()(users, many=True)
        ser = self.get_serializer(users, many=True)
        result = {
            'data': ser.data,
            'code': 200,
            "message": "OK"
        }
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # 创建序列化器
        ser = self.get_serializer(data=request.data)
        # 校验请求数据
        if ser.is_valid():
            # 校验通过，则添加数据到数据
            ser.save()
            return Response({'code': 201, 'data': ser.data, "message": 'OK'})
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(GenericAPIView):
    # 设置模型类
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = 'id'

    def get(self, request, id, format=None):
        obj = self.get_object()
        ser = self.get_serializer(obj)
        return Response({'code': 200, "data": ser.data, 'message': "OK"}, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        obj = self.get_object()
        # 修改单个用户资源
        ser = self.get_serializer(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'code': 200, "data": ser.validated_data, "message": "OK"}, status=status.HTTP_200_OK)
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        obj = self.get_object()
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

```

#### 6、mixins类

ListModelMixin

- list()

CreateModelMixin

- create()

RetrieveModelMixin

- retrieve()

DestoryModelMixin

- destory()

UpdateModelMixin

- update()

```python
class UserListView(GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    # 设置模型类
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailView(GenericAPIView,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    # 设置模型类
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

```

#### 7、扩展的视图类

```python
class UserListView(generics.ListAPIView,
                   generics.CreateAPIView):
    # 设置模型类
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserDetailView(generics.RetrieveAPIView,
                     generics.DestroyAPIView,
                     generics.UpdateAPIView):

    # 设置模型类
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = 'id'
```

8、viewset

ModelViewSet

```
A viewset that provides default `create()`, `retrieve()`, `update()`,`partial_update()`, `destroy()` and `list()` actions.
```

```python
class UserView(ModelViewSet):
    # 设置模型类
    queryset = UserInfo.objects.all()
    # 设置序列化器类
    serializer_class = UserInfoSerializer
    lookup_field = 'id'
```

```python

    path('users/', views.UserView.as_view({"get": 'list', 'post': 'create'})),
    path('users/<int:id>/', views.UserView.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'DELETE': "destroy"})),
```

