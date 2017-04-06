__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Считать одной строкой произвольное количество пар элементов "Название книги Число экземпляров", второй строкой название алгоритма хеширования md5
Aibolit 66 Barmaley 67
md5

Создать 2 класса:
1-й преобразует строку вида 'Aibolit 66 Babmaley 67', где название книги уникально, в словарь.
2-й осуществляет хеширования названия книги алгоритмом md5.
Вывести отдельными операторами вывода:
- элементы словаря, отсортированные по возрастанию ключа, например:
Aibolit 66
Barmaley 67
- результаты хеширования в виде пар названия алгоритма и результатов хеширования ключей, отсортированных по возрастанию,
представленных в шестнадцатеричном виде, сведенных в одну строку через пробел вида
md5 c47.... md5 5d....' (без пробелов в начале и конце строки).

Ответ должен выглядеть следующим образом:
Aibolit 66
Barmaley 67
md5 c47.... md5 5d....
Вариант
'''

import hashlib

s1 = 'Aibolit 66 Barmaley 67'
s2 = 'md5'

# s1 = input()
# s2 = input()


class Book:
    def __init__(self, line):
        keys = line.split()[::2]
        items = line.split()[1::2]
        self.cat = dict(zip(keys, items))

        #line = line.split()
        # self.cat = {}
        # for i in line:
        #     if line.index(i) % 2 == 0:
        #         self.cat[i] = None
        #         name = i
        #     else:
        #         self.cat[name] = int(i)

    def print_cat(self):
        for k, v in sorted(self.cat.items()):
            print('%s %s' %(k, v))

class Hashook(Book):
    def hash_maker(self, method):
        print_str = []
        for item in self.cat.keys():
            md = eval('hashlib.' + method)(item.encode())
            print_str.append('%s' % (md.hexdigest()))
        for i in sorted(print_str):
            print(method + " " + i,  end=' ')


bh = Hashook(s1)
bh.print_cat()
bh.hash_maker('md5')