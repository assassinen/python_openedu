__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps

# декораторы

# class A:
#     x=1
#     @classmethod
#     def get_x(cls):
#         print(cls.x)
#
# a = A()
# print(a.x)
# a.x = 5
# print(a.x)
# a.get_x()
#
# class B:
#     @staticmethod
#     def get_x():
#         print('staticmethod')
# b = B()
# b.get_x()
#
# class MyDecor1():
#     def __init__(self, f):
#         print('before function')
#         f()
#         print('after function')
#
#     def __call__(self):
#         print('Call')
#
# @MyDecor1
# def func1():
#     print('Function')
#
# func1()
#
#
# def mydecor2(func):
#     def decorated(*args, **kwargs):
#         print('before function')
#         result = func(*args, **kwargs)
#         print('after function')
#         return result
#     return decorated
#
#
# def x(a, b):
#     return a + b
#
# print('==============')
# xmydecor2 = mydecor2(x)
# print(xmydecor2)
# print(xmydecor2(5,6))
#
#
# @mydecor2
# def z(a,b):
#     return a - b
# def w(a=5, b=6):
#     return a/b
#
# print(z(9,5))
# print(w(10,5))
# print('==============')
#
# def mydecor3(hello='hello', bye='bye'):
#     def internal(func):
#         def decorated(*args, **kwargs):
#             print(hello)
#             result = func(*args, **kwargs)
#             print(bye)
#             return result
#         return decorated
#     return internal
#
# @mydecor3('one', 'two')
# def aa(a=5, b=4):
#     return a+b
#
# print(aa())
# print('==============')
#
# def paragraph(func):
#     def inner(*args, **kwargs):
#         print('<p>')
#         func(*args, **kwargs)
#         print('</p>')
#     return inner
#
# @paragraph
# def hello(text='Python'):
#     print('Hello ', text)
#
# hello()
# hello('c++')
# print('==============')


def mytag(tagname='p'):
    def decorator(func):
        def inner(*args, **kwargs):
            print('<%s>' %tagname)
            func(*args, **kwargs)
            print('<//%s>' %tagname)
        return inner
    return decorator

@mytag('p')
@mytag('b')
def hello(text='Python'):
    print('Hello ', text)

# hello()
hello('Java')
print('==============')

def paragraph(func):
    @wraps(func)
    def inner(text):
        print('<p>')
        func(text)
        print('</p>')
    return inner

@paragraph
def hello(text='Python'):
    print('Hello ', text)

hello('python')
print(hello.__name__)