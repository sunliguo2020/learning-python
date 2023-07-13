# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-04 13:21
"""


class Request(object):
    def __init__(self, obj):
        self.obj = obj

    @property
    def user(self):
        return self.obj.authticate()


class Auth(object):
    def __init__(self, name, age):
        self.name = name,
        self.age = age

    def authticate(self):
        return self.name


class APIView(object):
    def dispach(self):
        self.f2()

    def f2(self):
        a = Auth('alex', 18)
        b = Auth('oldboy', 18)
        req = Request(a)
        print(req.user)
        req = Request(b)
        print(req.user)


obj = APIView()
obj.dispach()
