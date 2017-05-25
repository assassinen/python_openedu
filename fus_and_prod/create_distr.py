__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

list_path = ('fast-d01(10.63.10.232)',
            'fast-d02(10.63.10.233)',
            'fast-m01(10.61.10.232)',
            'fast-m02(10.61.10.233)',
            'ffast-d01(10.63.10.230)',
            'ffast-d02(10.63.10.231)',
            'ffast-m01(10.61.10.230)',
            'ffast-m02(10.61.10.231)',
            'vfast-sp1(10.61.10.228)',
            'vfast-sp2(10.61.10.229)')

data_path = '20170526_'

for i in list_path:
    #print(data_path + i)
    os.mkdir(data_path + i)

