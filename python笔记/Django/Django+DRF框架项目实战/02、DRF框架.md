# DRF框架

## 一、DRF框架介绍

## 二、序列化器

## 三、请求和响应

## 四、视图集和路由

## 五、其他功能

## 1、认证&权限

## 2、限流

## 3、过滤

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



## 4、排序

## 5、分页

## 6、异常处理

## 7、文件上传

## 8、接口文档



## 六、ajax跨域

## 七、DRF JWT

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