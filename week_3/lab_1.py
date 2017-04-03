__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Ввести с клавиатуры строку латиницей (1-3 слова). Зашифровать ее с использованием гарантированных алгоритмов шифрования.
Сформировать словарь, где в качестве ключа используется название гарантированного алгоритма шифрования,
а в качестве значения - результат шифрования в шестнадцатеричном представлении { 'sha1': 'aaf4c…', 'md5', '5d4…',…}.
Итог вывести отдельными операторами вывода в виде пар ключа и значения, отсортированных по возрастанию ключа:
md5 5d414…
sha1 aaf4c…
Вариант
'''

import hashlib

methods = ['sha512', 'md5', 'sha1', 'sha224', 'sha256', 'sha384']
result = {}

def sorted_print(result):
    keys = list(result.keys())
    items = list(result.values())

    for value in sorted(result.values(), key=lambda str: len(str)):
        idx = items.index(value)
        print(keys[idx], items[idx])

#s = 'три слова'
s = input()

for method in methods:
    md = eval('hashlib.' + method)(s.encode())
    result[method] = md.hexdigest()


sorted_print(result)
for k, v in sorted(result.items()):
    print(k, v)