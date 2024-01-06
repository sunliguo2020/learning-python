from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.

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
