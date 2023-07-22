from rest_framework import mixins
from rest_framework import generics

from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.

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
