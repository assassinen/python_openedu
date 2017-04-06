__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A(object):
    x = 6
    def isAorB(self):
        return True
    def who(self):
        return 'parent'

class B(A):
    y = 7
    def who(self):
        return 'child'

a = A()
b = B()

print(a.x)
print(b.x)
print(b.y)
print(a.who())
print(b.who())
print(b.isAorB())


class B(A):
    def __init__(self):
        A.__init__(self)

b = B()
print(b.who())

class C(A):
    def __init__(self):
        super(C, self).__init__()

c=C()
print(c.who(), c.isAorB())

class A:
    def __init__(self):
        legs_before = 4
        legs_after = 2

class B(A):
    def __init__(self):
        legs_new = 4

zay = A()
zay2 = B()

print(zay.__dict__)
zay.legs2 = 2
print(zay.__dict__)


print(zay2.__dict__)

class A():
    eyes='green'

class B():
    eyes='blue'

class AB(A, B):
    legs = 4

class BA(B, A):
    legs = 4


ab = AB()
ba = BA()

print(ab.eyes)
print(ba.eyes)

print(ab.__class__)
print(type(ab))

print(isinstance(ab, AB))
print(isinstance(ab, A))

a = []
print(isinstance(a, list))
print(isinstance(a, str))

print(ab.__class__.__base__)
print(ba.__class__.__bases__[0].__base__)


class Object:
    def paint(self):
        print('Paint Object')

class Rectangle:
    def paint(self):
        print('Paint Rectangle')

class RectangleWithFill(Rectangle):
    def paint(self):
        super(RectangleWithFill, self).paint()
        #print('Fill')

r = RectangleWithFill()
r.paint()