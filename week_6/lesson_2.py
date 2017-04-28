__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# итераторы
def gen1():
    while True:
        yield 1

print(gen1())

def genlist1():
    alist1=range(5)
    for i in alist1:
        yield i*i

mygen = genlist1()
print("====")
print(mygen)
for i in mygen:
    print(i)

gens = gen1()
print(gens)
print(next(gens))
print(next(gens))


def gen():
    a = 1
    while a <= 10:
        yield a
        a += 1

gens = gen()
print(gens)
print(next(gens))
print(next(gens))
print(list(gens))
