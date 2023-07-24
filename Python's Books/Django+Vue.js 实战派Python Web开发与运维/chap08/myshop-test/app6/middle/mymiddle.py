# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-20 14:06
"""
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class AuthMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print('process_request1()方法执行')
        # return HttpResponse('返回')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('process_views1()方法执行')

    def process_template_response(self, request, response):
        print("process_template_response()1方法执行")
        return response

    def process_exception(self, request, exception):
        print('process_excepiton1()方法执行')

    def process_response(self, request, response):
        print('process_response1()方法执行，状态为', response.reason_phrase)
        return response


class AuthMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print('process_request2()方法执行')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('process_views2()方法执行')

    def process_template_response(self, request, response):
        print("process_template_response()2方法执行")
        return response

    def process_exception(self, request, exception):
        print('process_excepiton2()方法执行')

    def process_response(self, request, response):
        print('process_response2()方法执行，状态为', response.reason_phrase)
        return response
