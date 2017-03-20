__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#print ("This line will be printed.")
#Считать несколько имен людей одной строкой, записанных латиницей, через пробел, например:
str = input()
#Вывести их одной строкой в порядке возрастания «Anna Maria Peter».
print(" ".join(sorted(str.split())))
#Вывести их одной строкой в порядке убывания «Peter Maria Anna».
print(" ".join(sorted(str.split(), reverse=True)))
