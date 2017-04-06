__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A(object):
    x = 1

a = A()
print(a.x)
a.x = 5
print(a.x)
del (a.x)
print(a.x)

B=A
b=B()
print(b.x)


class C:
    x = 6
с = C()
print(с.x)
print('=====')

class Legs(object):
    count = 4
    def get_legs(self):
        return self.count
charlie=Legs()
print(charlie.count)
print(charlie.get_legs())
charlie.count-=1
print(charlie.get_legs())
del charlie.count
print(charlie.get_legs())

#удаление класса не приводит к удалению объекта
print(type(a))

class A:
    __x = 1
    def __priv(self):
        print('private metod')

a = A()
print(a._A__x)
a._A__x = 6
print(a._A__x)
print(dir(a))
a._A__priv()


class A:
    __slots__ = ('r', 'i') #ограничивает свойства
    def __init__(self, x=2, y=3):
        self.r = x
        self.i = y

comp1=A(4,5)
print(comp1.r)
print(comp1.i)
comp2=A()
print(comp2.r)
print(comp2.i)
# comp2.tt = 8
# print(comp2.tt)
print('==========')

class Legs(object):
    def __init__(self, x=4):
        self.count = 4

    def get_legs(self):
        print(self.count)

    def tramLegs(self):
        self.count -= 2

    def aibolit(self):
        self.count += 1

    def __del__(self):
        print('Delete object')

z = Legs()
z.get_legs()
z.tramLegs()
z.get_legs()
z.aibolit()
z.aibolit()
z.get_legs()

del z

class Object:
    def paint(self):
        print('Paint Object')

class Rectangle:
    def paint(self):
        print('Paint Rectangle')

class RectangleWithFill(Rectangle):
    def paint(self):
        super(RectangleWithFill,self).paint()
        print('Fill')

obj_list = [Object(), Rectangle(), RectangleWithFill()]
print(obj_list)

for i in obj_list:
    i.paint()

obj_dict = {'obj': Object(), 'rec': Rectangle(), 'rwf': RectangleWithFill()}
for key, val in enumerate(obj_dict):
    print(key, val)

print('=============')
for key, val in enumerate(obj_dict):
    obj_dict[val].paint()


class A:
    def __init__(self, x, y):
        self.x = x + y
    def __call__(self, x, y):
        return x + y

a = A(5, 5)
print(a.x)
print(a(5,7))