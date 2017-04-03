__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f0 (x, y, z=1):
    return (x+y)**z
a = [1, 2, 3]
print(f0(*a))

def f1(x):
    return x**2

#функция f1 выполняется для списка a
def f2(*args):
    return list(map(f1, args))

print(f2(5, 6, 7))

def f3(*args):
    print(args)
f3(5, 6, 7)

def f4(**kwargs):
    for key, item in kwargs.items():
        print(key, item)

def f5(**kwargs):
    for key, item in enumerate(kwargs.items()):
        print(key, item)

f4(a='aa', b='bb', c='cc')
f5(a='aa', b='bb', c='cc')

def f6 (*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

b = dict(a='aa', b='bb', c='cc')
f6(1, 'aa', 3, 4, a='3', b=7)
f6(*a, **b)

f7=f6
f7(4, f = 5)

def plus(x,y):
    return x + y
def minux(x,y):
    return x - y

list_def = [plus, minux]
print(list_def[0](5,6))

dict_def = {'+': plus, '-': minux}
print(dict_def['-'](9,5))

def func(x, y):
    def plus(x, y):
        return x + y
    def minux(x, y):
        return x - y

    if x > y:
        return minux(x,y)
    else:
        return plus(x, y)

print(func(1,2))
print(func(5,2))
