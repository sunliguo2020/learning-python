# -*- coding: utf-8 -*-

from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response({"status": True})


class MessageView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.query_params)
        return Response({'code':''})
