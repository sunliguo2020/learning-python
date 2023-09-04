from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
@api_view(['GET'])
def get_data(request):
    params = request.query_params
    return Response({}, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', 'PATCH'])
def add_data(request):
    pass


class DemoView(APIView):
    def get(self, request):
        return Response({'code': 'get-ok'})

    def post(self, request):
        return Response({'code': 'post-ok'})

    def put(self, request):
        return Response({'code': 'put-ok'})

    def putch(self, request):
        return Response({'code': 'putch-ok'})

    def delete(self, request):
        return Response({'code': 'delete-ok'})
