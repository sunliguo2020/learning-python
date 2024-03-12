# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-09 17:40
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class CustomResponse(Response):
    def __init__(self, data=None, code=None, msg=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None,
                 **kwargs):
        super().__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        self.data = {'code': code, 'message': msg, 'data': data}
        self.data.update(kwargs)
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in headers.items():
                self[name] = value
