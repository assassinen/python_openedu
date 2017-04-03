__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

print(dir(hashlib))

s = '1245'
print(s)
b_s = s.encode()
print(b_s)
md = hashlib.md5(b_s)
print(md.hexdigest())

h1=hashlib.md5(b'Python')
p1=h1.hexdigest()
print(p1)

s1='Питон'
print(s1.encode('utf-8'))
print(s1)

s1='Питон'
print(s1.encode('koi8-r'))
print(s1)