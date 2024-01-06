





### Mixin.CreteaModelMixin

创建一个模型实例

  用到：self.get_serializer()

```python

class CreateModelMixin:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        pass
```

### Mixin.ListModelMixin

列出查询集

用到：

```
self.get_queryset()
self.get_serializer()
```

```python
class ListModelMixin:
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
       pass
```

### Mixin.RetrieveModelMixin

检索一个模型实例

用到：

```
self.get_object()
self.get_serializer()
```

### Mixin.DestroyModelMixin

```python
class DestroyModelMixin:
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        pass
```

### Mixin.UpdateModelMixin

更新模型实例

用到：

self.get_object()

self.get_serializer()

```python

class UpdateModelMixin:
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        pass
```



