__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
строки - не изменяемы
варианты объявления:
'''

a='i love python'

print('получить первых 4 символа с помощью срезов')
print(a[:4])
print(a[0:4])
#print(a[1:4])
#print(a[1:5])
#print(a[:5])
print(a[0:4:1])

print('получить первых 4 символа с помощью подстановочных символов')
print('%.4s'%a)
#print('%4.s'%a)
#print('%4.r'%a)
#print('%4s'%a)
#print('%4r'%a)
#print('%4f'%a)

print('получить первых 4 символа с помощью метода format')
print('{:.4}'.format(a))
#print('{:.5}'.format(a))
#print('{:4.}'.format(a))
#print('{:.5}'.format(a))
print('{:1.4}'.format(a))
#print('{:0.4}'.format(a))

# b = """123456"""
# print(b[2:])
# print(b[0:-4])
# print(b[2:-4])
# print(b.replace('34', '43'))
#
# print("%2ss"%b)