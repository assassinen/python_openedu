__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


alist = list(range(1,6))
print(alist)
aiter = iter(alist)
print(aiter)
#print(list(aiter))
diter = iter({'a': 1, 'b': 2})
print(diter)
#print(dict(diter))


# for i in diter:
#     print(i)

a = [x for x in range(10)]
print(a)
b = itertools.accumulate(a)
print(b)
print(list(b))

print("====")

print(list(itertools.combinations('abcsvvb', 2)))
print(list(itertools.combinations_with_replacement('abcsvvb', 2)))
print(list(itertools.permutations('abc')))

a = [1,2,5,6,1,3]
print(list(itertools.dropwhile(lambda x: x < 4, a)))
print(list(itertools.filterfalse(lambda x: x < 4, a)))
print(list(itertools.takewhile(lambda x: x < 4, a)))

print(list(itertools.product('abc','xy')))
print(dict(itertools.product('abc','xyz')))

