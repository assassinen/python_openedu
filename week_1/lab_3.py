__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Считать единой строкой без пробелов набор целых чисел (28745623873465386),
#str = input()
str = '28745623873465386'
# удалить все дубликаты,
l = []
for i in str:
    if int(i) not in l:
        l.append(int(i))
# вывести отдельными операторами вывода в порядке возрастания и
print(tuple(sorted(l)))
# в порядке убывания в виде кортежей целых чисел (1,2,3,4) и (4,3,2,1).
print(tuple(sorted(l, reverse=True)))
print()
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)

