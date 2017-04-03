__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Считать отдельными операторами целочисленные ширину и высоту прямоугольника, создать функцию (def), принимающую в качестве параметров ширину и высоту фигуры.
Внутри функции создать две вложенные функции (lambda) по подсчету площади и периметра фигуры.
Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например '38 90').
'''


def rectangle(a, b, name='perimeter'):
    f = [lambda a, b: (a + b) * 2, lambda a, b: a * b]
    s = {'3': lambda a, b: (a + b) * 2, '4': lambda a, b: a * b}


    if name == 'perimeter':
        return f[0](a,b)
    else:
        return s['4'](a,b)

#a = int(input())
#b = int(input())

a = 5
b = 6

print(rectangle(a, b, name=''), rectangle(a, b, name='perimeter'))
