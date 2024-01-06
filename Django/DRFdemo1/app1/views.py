from rest_framework.viewsets import ModelViewSet

from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.

class UserView(ModelViewSet):
    # 设置模型类
    queryset = UserInfo.objects.all()
    # 设置序列化器类
    serializer_class = UserInfoSerializer
    lookup_field = 'id'


