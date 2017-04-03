__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import pickle
import shutil

# print(sys.platform)
# print(sys.version)
#
# old_dir = os.getcwd()
# print(old_dir)
# print(os.listdir())
#
# os.chdir('c:\\')
# print(os.getcwd())
# os.chdir(old_dir)
# print(os.getcwd())
#
# #os.mkdir('test')
os.chdir('test')
print(os.getcwd())

f2 = open('f2.txt', 'w', encoding="utf8")
f2.write('Ежик шел по лесу и ел яблоко\n')
f2.write('Лес шел по яблоку и ел ежика')

f2.close()

f3 = open('f2.txt', 'r+', encoding="utf8")
print(f3.read())
f3.seek(0)      #возврат к началу файла
print(f3.read(10))

f3.seek(0)      #возврат к началу файла
for line in f3:
    print(line)

f3.close()

f4 = open('f2.txt', 'r+', encoding="utf8")
f5 = open('f5.txt', 'w', encoding="utf8")

s1=f4.read().split()
print(s1)
s1.sort()
f5.write(' '.join(s1))

f4.close()
f5.close()

print(s1)

a1 = list(range(10))
print(a1)
s = pickle.dumps(a1)
del a1
try:
    print(a1)
except:
    a2 = pickle.loads(s)
    print(a2)

print(os.listdir())


name = 'C:\shareFolder\Dropbox\python_openedu'
print(os.listdir(name))

def f1(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
        else:
            f1(path)

f1(name)

if os.path.exists('t1'):
    shutil.rmtree('t1')
os.makedirs('t1/t2/t3')
print(os.path.exists('t1/t2/t3'))

shutil.copy('f5.txt', 't1/t2/f5_1.txt')
shutil.copy('f5.txt', 't1/f5_2.txt')
shutil.move('t1/f5_2.txt', 't1/t2/t3')
shutil.move('t1/t2/f5_1.txt', 't1/t2/t3/5_new.txt')


filenames = os.listdir()
print(filenames)
for i in filenames:
    print(os.path.abspath(i))

print('текущая папка')
print(os.getcwd())


os.chdir('../')
print(os.getcwd())




