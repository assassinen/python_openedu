__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import reduce

a=list(range(5))
a1=reduce(lambda x,y:x*y,a)

print(a1)


f2 = lambda x,y : x+y
print(f2(5,5))

a = [1, 2, 3, 4]
a=list(map(lambda x:x**2,a))
print(a)
print('=====')
print(list(map(lambda x: x*x, a)))
print((lambda x: x*x)(4))
print([(lambda x: x*x)(x) for x in a])

f3 = lambda x=5, y=6 : x+y
print(f3())

print()
a = [lambda x: x**1, lambda x: x**2]
for i in a:
    print(i(5))
print(a[1](8))

d = {'0': lambda x: x**0, '2': lambda x: x**2}
print(d['2'](8))


c = (lambda x, y: x if x < y else y)
print(c(8,5))


def summ(x,y):
    return x+y

#summ_car = lambda x: lambda y: summ(x,y)
summ_car = lambda x: lambda y: x+y
print(summ_car(5)(2))