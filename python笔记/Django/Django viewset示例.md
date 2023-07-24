模型类

```python
class PersonId(BaseModel, models.Model):
    personid = models.CharField(verbose_name="personid", max_length=32)
    idcard = models.CharField(verbose_name="身份证号", max_length=18)

    class Meta:
        db_table = 'peronsid'
        verbose_name = '分析后的personid'
        verbose_name_plural = verbose_name
        unique_together = ['personid', 'idcard']

```

序列化类

```python
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from api.models import PersonId


class PersonidModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonId
        fields = ['id', 'idcard', 'personid']

        validators = [
            UniqueTogetherValidator(queryset=PersonId.objects.all(),
                                    fields=('personid', 'idcard'),
                                    message='已经有重复的personid和idcard')]

```

views

```python
from rest_framework.viewsets import ModelViewSet

from api.models import PersonId
from api.serializers import PersonidModelSerializer


# Create your views here.


class PersonidView(ModelViewSet):
    queryset = PersonId.objects.all()
    serializer_class = PersonidModelSerializer

```

urls

```python
path('personid/', PersonidView.as_view({'get': 'list',
                                            'post': 'create',
                                            })),
path('personid/<int:pk>/', PersonidView.as_view({"get": "retrieve",
                                                     "put": 'update',
                                                     "delete": "destroy"}))

```

