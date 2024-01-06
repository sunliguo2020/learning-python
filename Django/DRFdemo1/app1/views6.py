from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.

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
