__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Создайте кортеж a из одного элемента 5

a=(5,)
print(a)
a=(5)
print(a)
#a=tuple(5)
print(a)
#a=tuple(5,)
print(a)
a=5
print(a)


print('Дан кортеж от 0 до 10, вывести в обратном порядке')
a = tuple(range(11))

print(a[::-1])
print(a[0:-1:-1])
print(a[-1:0:-1])
print(a[::1])
print(a[-1:0:])