__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a='hello word python'
c='{1} {2} {0}'.format(*a.split())
print(c)

print('==============')

# a='hello word python'
# b=list('abc')
# c=dict(zip(a.split(),))
# d='{a} {b} {c}'.format(**c)
# print(d)


a=[1, 3, 5, 2, 4]
print(reversed(a))
print(a)

print('==============')

def summa(a,b):
    return a+b
a=summa('4','4')
print(a)

