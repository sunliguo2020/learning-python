from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import UserInfo
from .serializers2 import UserInfoSerializer


# Create your views here.

class UserListView(APIView):
    def get(self, request, format=None):
        pass

    def post(self,request,format = None):
        pass


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
        ser = UserInfoSerializer(users, many=True)
        result = {
            'data': ser.data,
            'code': 200,
            "message": "OK"
        }
        return JsonResponse(result)
    elif request.method == 'POST':
        a = {"id": 1, "name": "sunliguo", "pwd": "123435", "email": "1234@qq.com", "age": 10
             }
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
        return JsonResponse({'code': 405, 'messae': f"不支持该请求{request.method}"})
