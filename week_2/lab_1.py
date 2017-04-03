__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Считать отдельными операторами целочисленные ширину и высоту прямоугольника.
Создать функцию (def), принимающую в качестве параметров ширину и высоту фигуры и название функции, которую необходимо выполнить.
Имя вложенной функции передавать явным образом (например: (a,b,name='perim')).
Внутри функции создать две вложенные функции (def) по подсчету площади и периметра фигуры.
Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например, '38 90').
'''

def rectangle(a, b, name='perimeter'):
    def perimeter(a, b):
        return (a + b) * 2
    def space(a, b):
        return a * b

    if name == 'perimeter':
        return perimeter(a, b)
    else:
        return space(a, b)


a = int(input())
b = int(input())

print(rectangle(a, b, name='perimeter'), rectangle(a, b, name=''))
