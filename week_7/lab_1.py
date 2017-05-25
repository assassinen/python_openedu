__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# import sqlite3
# con = sqlite3.connect('books01.db')
# con.close()


# import sqlite3
# import os
# os.chdir(r'C:\shareFolder\Dropbox\python_openedu\week_7')
# print(os.getcwd())
# con=sqlite3.connect('books01.db')
# con.close()
#
#
# import sqlite3
# import os
# #os.chdir(r'g:\sqlite_opros_6')
# con=sqlite3.connect('books02.db')
# cur=con.cursor()
# sql='''
# CREATE TABLE IF NOT EXISTS author  (
#     id_author INTEGER PRIMARY KEY AUTOINCREMENT,
#     author_name TEXT,
#     author_descr TEXT
# );
# '''
# cur.executescript(sql)
# cur.close()
# con.close()


# import sqlite3
# import os
# #os.chdir(r'g:\sqlite_opros_6')
# con=sqlite3.connect('books02.db')
# cur=con.cursor()
# sql='''
# CREATE TABLE IF NOT EXISTS author  (
#     id_author INTEGER PRIMARY KEY AUTOINCREMENT,
#     author_name TEXT,
#     author_descr TEXT
# );
# CREATE TABLE IF NOT EXISTS style  (
#     id_style INTEGER PRIMARY KEY AUTOINCREMENT,
#     style_name TEXT
# );
# CREATE TABLE IF NOT EXISTS book  (
#     id_book INTEGER PRIMARY KEY AUTOINCREMENT,
#     id_author INTEGER,
#     id_style INTEGER,
#     title TEXT,
#     description TEXT,
#     number_ex INTEGER
# );
# '''
# cur.executescript(sql)
# cur.close()
# con.close()


# import sqlite3
# import os
# #os.chdir(r'g:\sqlite_opros_6')
# con=sqlite3.connect('books02.db')
# cur = con.cursor()
# sql = """\
# INSERT INTO author (author_name, author_descr)
# VALUES ('Chukovskiy', 'Pisatel')
# """
#
# cur.executescript(sql)
# cur.close()
# con.commit()
# con.close()


# import sqlite3
# import os
# #os.chdir(r'g:\sqlite_opros_6')
# con=sqlite3.connect('books02.db')
# cur = con.cursor()
# sql = """\
# select * from  author
# """
#
# cur.executescript(sql)
# cur.close()
# con.commit()
# con.close()

import sqlite3
import os
#os.chdir(r'g:\sqlite_opros_6')
con=sqlite3.connect('books02.db')
cur=con.cursor()
sql='''
CREATE TABLE style IF NOT EXISTS (
    id_style INTEGER PRIMARY KEY AUTOINCREMENT,
    style_name TEXT
);'''
cur.executescript(sql)
cur.close()
con.close()