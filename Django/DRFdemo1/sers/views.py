from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book


# Create your views here.
class BookSerializers(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.IntegerField()
    put_date = serializers.DateField()

    def create(self, validated_data):
        return Book.objects.create(**self.validated_data)

    def update(self, instance, validated_data):
        # 更新逻辑
        # 方式一：
        # instance.title = validated_data['title']
        # instance.price = validated_data['price']
        # instance.put_date = validated_data['put_date']
        #
        # instance.save()
        # # print(type(instance)) # <class 'sers.models.Book'>
        # # print(instance)     # Book object (11)
        # # print(dir(instance))
        # # instance.update(**validated_data) # 模型类实例没有update方法
        # return instance

        # 方式二：
        Book.objects.filter(pk=instance.id).update(**self.validated_data)
        updated_book = Book.objects.get(pk=id)

        return updated_book


class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookView(APIView):
    def get(self, request):
        print(request.GET)
        # print(request.POST)
        print(request.body)  # You cannot access body after reading from request's data stream
        # 获取所有的书籍
        queryset = Book.objects.all()
        # 构建序列化对象
        # ser = BookSerializers(instance=queryset, many=True)
        ser = BookModelSerializers(instance=queryset, many=True)
        return Response(ser.data)

    def post(self, request):
        # 获取请求数据
        print("data", request.data)
        # 构建序列化对象
        serializer = BookSerializers(data=request.data)
        # serializer = BookModelSerializers(data=request.data)
        if serializer.is_valid():
            # 校验通过，数据插入数据库
            # Book.objects.create(**serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BookDetailView(APIView):
    """
    查看单一资源
    """

    def get(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            ser = BookSerializers(instance=book)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_302_FOUND)
        else:
            return Response(ser.data)

    def delete(self, request, id):

        result = Book.objects.filter(id=id).delete()
        print(result)

        return Response()

    def put(self, request, id):
        """
        修改一本书籍
        """
        try:
            # 查询是否存在该资源
            book = Book.objects.get(id=id)

        except Exception as e:
            return Response(data={"error": str(e)})
        else:
            ser = BookSerializers(data=request.data, instance=book)
            if ser.is_valid():
                Book.objects.filter(id=id).update(**ser.validated_data)
                updated_book = Book.objects.get(pk=id)
                ser.instance = updated_book
                # ser.save()
                return Response(ser.validated_data)
            else:
                return Response(ser.errors)
