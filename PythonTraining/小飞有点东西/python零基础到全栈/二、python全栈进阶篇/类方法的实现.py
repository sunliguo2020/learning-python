# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-23 14:39
"""
import settings


class Mysql:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def f1(self):
        print(self.ip, self.port)

    @staticmethod
    def f2(self):
        pass

    @classmethod
    def instance_from_conf(cls):
        print(cls)
        obj = cls(settings.IP, settings.PORT)

        return obj


if __name__ == '__main__':
    obj = Mysql.instance_from_conf()
    print(obj.__dict__)

    print(obj.f1)
    print(Mysql.f1)
    print(obj.f2)
    print(Mysql.f2)
    print(obj.instance_from_conf)
    print(Mysql.instance_from_conf)
