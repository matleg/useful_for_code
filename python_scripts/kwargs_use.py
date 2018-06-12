#!/usr/bin/python
# -*- coding: utf8 -*-


class Foo(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        for b in kwargs:
            self.b=kwargs[b]
            print(self.b)
        pass

    def print_kwargs(self):
        for a in self.kwargs:
            print(a, self.kwargs[a])
        print(self.b)


ff = Foo(a=3, b=4, c=5, d=6)

ff.print_kwargs()
