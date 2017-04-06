__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Создайте класс, осуществляющий подсчет и изменение числа книг. Названия книг, их количество считываются одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
В классе должен быть реализован конструктор, деструктор, методы просмотра числа, взятия и возвращения книг.
Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1 книге с выводом текущего числа после вызова каждого из методов, меняющих значение книг.
Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'.
'''

s = 'Boogeyman 66 Battleground 50'
#s = input()

class Book:
    def __init__(self, line):
        line = line.split()
        self.cat = {}
        for i in line:
            if line.index(i) % 2 == 0:
                self.cat[i] = 0
                name = i
            else:
                self.cat[name] = int(i)

    # def __init__(self, data):
    #     line = data.split()
    #     self.cat = {k: int(v) for k, v in zip(line[::2], line[1::2])}

    def __iter__(self):
        return iter(self.cat)

    def count_book(self, book_name):
        return self.cat[book_name]

    def book_names(self):
        return self.cat.keys()

    def take_book(self, book_name, n = 1):
        self.cat[book_name] = self.cat[book_name] + n

    def give_book(self, book_name, n = 1):
        self.cat[book_name] = self.cat[book_name] - n

    def __del__(self):
        pass


b = Book(s)

for book_name in b.cat:
    print(book_name, end=" ")
    print(b.count_book(book_name), end=" ")
    b.give_book(book_name)
    print(b.count_book(book_name), end=" ")
    b.take_book(book_name)
    print(b.count_book(book_name), end=" ")

# print('Boogeyman', end=" ")
# print(b.count_book('Boogeyman'), end=" ")
# b.give_book('Boogeyman')
# print(b.count_book('Boogeyman'), end=" ")
# b.take_book('Boogeyman')
# print(b.count_book('Boogeyman'), end=" ")
#
# print('Battleground', end=" ")
# print(b.count_book('Battleground'), end=" ")
# b.give_book('Battleground')
# print(b.count_book('Battleground'), end=" ")
# b.take_book('Battleground')
# print(b.count_book('Battleground'), end=" ")
#
