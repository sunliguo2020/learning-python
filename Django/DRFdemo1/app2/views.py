from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
@api_view(['GET'])
def get_data(request):
    params = request.query_params
    return Response({}, status=status.HTTP_200_OK)


class DemoView(APIView):
    def get(self, request):
        return Response({'code': 'get-ok'})
