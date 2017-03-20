__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Функция
# def f(a,b):
# ... return a+b
#
# применима:
#  к целым числам  к вещественным числам  к спискам  к строкам  к словарям
# - Этот вопрос оставлен без ответа.
# Даны три функции:
# 1.
#
# >>> def f1(a,b):
# 	return a+b
# 2.
# >>> def f2(a,b):
# 	print(a+b)
# 3.
# >>> def f3(a,b):
# 	global summ
# 	summ=a+b
#
# Какая из функций отвечает правилам функционального программирования?
#  ни одна  1  1 и 2  1 и 3  все
# Каким из приведенных способов возможно применение функции

def f4(x):
    return x**2

#к элементам списка
a=list(range(5))
print(a)
b=[f4(i) for i in a]
print(b)
for i in a:
    i=f4(i)
    print(i, end=" ")
print()
for i in a:
    i=f4(i)
    print(i, end=" ")
print()
a=list(map(f4,a))
print(a)
#a=(map(f4,a)
#print(a)
