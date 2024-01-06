# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-11-24 19:31
"""


class ContextMixin:
    """
    A default context mixin that passes the keyword arguments received by
    get_context_data() as the template context.
    """

    extra_context = None

    def get_context_data(self, **kwargs):
        kwargs.setdefault("view", self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs


class MultipleObjectMixin(ContextMixin):
    allow_empty = True
    ordering = "cdsdd"
    extra_context = {"a": "我是谁"}

    def get_ordering(self):
        return self.ordering
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context
    def print_context_data(self):
        print(self.extra_context)

if __name__ == "__main__":
    a = MultipleObjectMixin()
    # print(a.get_ordering())
    # print(a.ordering)
    # print(MultipleObjectMixin.ordering)
    # print(a.get_context_data())
    a.print_context_data()
    b = MultipleObjectMixin()
    b.extra_context = {'b':"b"

    }
    b.print_context_data()
    MultipleObjectMixin.extra_context = {
        'c':"c"

    }
    a.print_context_data()
    b.print_context_data()