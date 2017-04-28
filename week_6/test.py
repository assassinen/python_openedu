__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arr = range(5)
a = [i for i in arr]
b = (i for i in arr)

print(a)

a = 'asd'
c = a[::-1]
print(a[::-1])
print(c)

a = [1,2,3,4]
b = str(a)
print(b)
print(b+'x')

s = '1'
print(''.join(map(str, a))+'x')

print(type(b))

a = [1,3]
print(id(a))
a += [2]
print(id(a))

print(a)