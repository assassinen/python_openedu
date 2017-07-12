__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from xml.etree import ElementTree


#print(os.getcwd())
print(dir(ElementTree))


file_route = 'C:\share\TestFAST\ptest_internet\configuration.xml'
file1 = open(file_route, 'r')
tree = ElementTree.parse(file1)
root = tree.getroot()
# print(root)
# print(root.tag)
# print(root.attrib)

# for i in root:
#     print(i.tag, i.attrib)

# for i in tree.iter():
#     print(i.text)

# for i in tree.iter('ip'):
#     print(i.attrib, i.text)

# for i in root:
#     print(i.attrib)
#     for a in i.attrib:
#         print(a)
#     if i.attrib == "FUT-BOOK-1":
#         print(123)
#         print(i)


# for i in root.findall('MarketDataGroup'):
#     for j in i.findall('connections'):
#         for x in j.findall('connection'):
#             print(x.find('ip').text, x.find('port').text)
#             # for y in x.findall('ip'):
#             #     print(y.text)
#
# print(root[1][0][0][3].text)

# for i in tree.iter('port'):
#     tree.remove(i)

connections = ElementTree.Element('new_cont')
type = ElementTree.SubElement(connections, 'new_c').set('bb', 'aa')
ElementTree.dump(connections)

tree.write('C:\share\TestFAST\ptest_internet\configuration_1.xml')

file1.close()