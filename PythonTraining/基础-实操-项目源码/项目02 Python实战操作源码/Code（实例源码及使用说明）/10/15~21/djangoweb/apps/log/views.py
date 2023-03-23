import logging

from django.shortcuts import render, HttpResponse
from django.views.generic import View

# Create your views here.
# 为logger命名
logger = logging.getLogger('log.log')


class CreateLog(View):
    """日志配置Demo"""

    def get(self, request):
        # 发起调用
        logger.error('Something went wrong!')
        return HttpResponse('c0c')
