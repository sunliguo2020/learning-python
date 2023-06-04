# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-04 9:21
"""
from collections.abc import Iterable


class A:
    def __iter__(self):
        return self


print(isinstance(iter(A()), Iterable))
