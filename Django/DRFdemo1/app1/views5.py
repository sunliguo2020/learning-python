from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.

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
