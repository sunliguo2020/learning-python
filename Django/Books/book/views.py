import json

from django.contrib.auth import login, logout, authenticate
from django.db import transaction
from django.http import JsonResponse
from django.views import View

from book.models import Books, Record


# Create your views here.
class LoginView(View):
    def post(self, request):
        """登录接口
        获取参数（表单/json)
        request.POST 获取表单参数
        request.body 获取json数据
        """
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # 前端表单传参 x-www-form-urlencoded
        # print(request.POST) # <QueryDict: {'username': ['username'], 'password': ['password']}>
        # print(request.body) # b'username=username&password=password'
        # 前端json传递
        # print(request.POST) # <QueryDict: {}>
        # print(request.body) # b'{\r\n    "username":"username",\r\n    "password":"password"\r\n}'

        # 获取参数
        params = request.POST if len(request.POST) else json.loads(request.body.decode('utf-8'))

        print(params)
        username = params.get('username')
        password = params.get('password')

        # 校验账号密码是否正确
        user = authenticate(username=username, password=password)
        if user:
            # 保存登录的信息到session
            login(request, user)
            return JsonResponse({'code': 1000, "message": "登录成功"})
        else:
            return JsonResponse({'code': 2001, "message": "登录失败，账号或密码不对！"}, status='403')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return JsonResponse({"code": 200, "message": '已注销用户登录！'})


class BookView(View):
    """图书管理的接口

    需求：给图书管理登录
    """

    def get(self, request):
        """获取图书列表"""
        # 判断是否登录
        if not request.user.is_authenticated:
            return JsonResponse({"code": 2002, "message": "认证失败，没有访问权限！"})

        bs = Books.objects.all()
        data = []
        for b in bs:
            dic = {"id": b.id,
                   "name": b.name,
                   "status": b.status}
            data.append(dic)
        return JsonResponse({"code": 1000, "message": "获取成功", "data": data})

    def post(self, request):
        """添加图书"""
        # 判断是否登录
        if not request.user.is_authenticated:
            return JsonResponse({"code": 2002, "message": "认证失败，没有访问权限！"})
        # 获取参数 (同时支持json和表单参数）
        params = request.POST if len(request.POST) else json.loads(request.body.decode('utf-8'))
        id = params.get('id')
        name = params.get('name')
        # 3、参数校验
        if not (id and name):
            return JsonResponse({"code": 2001, "message": "书籍的id和name不能为空！"})
        # 校验id是否存在
        try:
            Books.objects.create(id=id, name=name)
        except Exception as e:
            return JsonResponse({"code": 2001, "message": "书籍编号已存在！"})

        return JsonResponse({"code": 1000, "message": "添加成功！"})

    def delete(self, request):
        """删除图书"""
        # 1、校验用户是否已经登录
        if not request.user.is_authenticated:
            return JsonResponse({"code": 2002, "message": "认证失败，没有访问权限！"})
        # 2、获取参数（删除的书籍id）
        id = request.GET.get('id')
        if not id:
            return JsonResponse({"code": 2002, "message": "删除书籍id是必选项！"})

        # 3、校验参数是否有效
        try:
            book = Books.objects.get(id=id)
        except Exception as e:
            return JsonResponse({"code": 2002, "message": "传递的id有误！"})
        else:
            book.delete()
            return JsonResponse({"code": 2002, "message": "删除成功！"})


class RecordView(View):
    """
    借书
    """

    def post(self, request):
        # 1、登录权限
        if not request.user.is_authenticated:
            return JsonResponse({"code": 2002, "message": "认证失败，没有访问权限！"})
        # 2、获取参数
        params = request.POST if len(request.POST) else json.loads(request.body.decode('utf-8'))
        book_id = params.get('book')
        name = params.get('name')

        if not (book_id and name):
            return JsonResponse({"code": 2002, "message": "书籍编号(book)和借书人(name)名字不能为空！"})

        # 校验书籍编号是否正确
        try:
            book = Books.objects.get(id=book_id)
        except Exception as e:
            return JsonResponse({"code": 2002, "message": "书籍编号有误！"})
        if book.status:
            return JsonResponse({"code": 2002, "message": "书籍已经借出！"})

        # 4、借书操作
        # 修改书籍状态
        with transaction.atomic():
            book.status = True
            book.save()
            # 添加一条借书记录
            Record.objects.create(book=book, name=name)

        return JsonResponse({"code": 2002, "message": "借书成功！"})
