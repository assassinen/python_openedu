__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

alist = [{'a':[1,2,3], 'b':(1,2,3), 'c':{'a':'List','b':'Data'}, 'd':3.14}]
print(alist)

json_list = json.dumps(alist)
print(json_list)

json_list = json.dumps(alist, separators=(',',':'))
print(json_list)

json_list = json.dumps(alist, separators=(',',':')mc)
print(json_list)

json_list = json.dumps(alist, separators=(',',':'), indent=4, sort_keys=True)
print(json_list)

alist_2 = json.loads(json_list)
print(alist)
print(alist_2)