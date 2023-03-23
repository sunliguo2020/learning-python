from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import View


def receive_message(request):
    """接收消息"""

    # 获取消息
    storage = messages.get_messages(request)
    for message in storage:
        print(message)
    return HttpResponse('请在控制台查看消息')


class TipView(View):
    """信息提示"""

    def get(self, request):
        """两种添加提示信息的方式，五种信息类型"""

        messages.debug(request, '调试信息')
        messages.add_message(request, messages.INFO, '提示信息')
        messages.success(request, '成功信息')
        messages.warning(request, '警告信息')
        messages.error(request, '错误信息')
        return render(request, 'message.html', locals(), RequestContext(request))
