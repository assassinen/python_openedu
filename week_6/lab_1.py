__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Лаборатория
Считать с клавиатуры отдельными операторами:
- заголовок страницы (например, Hello);
- цвет заголовка первого уровня (например, blue);
- цвет текста абзаца (например, red);
- текст заголовка первого уровня (например, Title 1);
- текст статьи (например, Article text).

Использовать только латинские символы.
Используя декораторы, сформировать текст html-страницы для публикации статьи.

Пример входного потока:
Hello
blue
red
Title 1
Article text

Пример выходного потока:
<html>
<head>
<title>Hello</title>
<style>h1{color:blue}p{color:red}</style>
</head>
<body>
<h1>Title 1</h1>
<p>Article text</p>
</body>
</html>
'''


# title_s = 'Hello'
# h1_color_s = 'blue'
# p_color_s = 'red'
# h1_s = 'Title 1'
# p_s = 'Article text'

input_data = ['Hello', 'blue', 'red', 'Title 1', 'Article text']

# input_data = []
# for i in range(5):
#     input_data.append(input())


def mytag(tagname='p'):
    def decorator(func):
        def inner(*args, **kwargs):
            if tagname in ['html', 'head', 'body']:
                break_line = '\n'
            else:
                break_line = ''
            if tagname not in ['h1_color', 'p_color']:
                print('<%s>' %tagname, end=break_line)
                func(*args, **kwargs)
                print('</%s>' %tagname)
            else:
                print('%s{color:' %tagname[0:-6], end=break_line)
                func(*args, **kwargs)
                print("}", end=break_line)
        return inner
    return decorator


@mytag('html')
def hello(*args):
    head(*args)
    body(*args)

@mytag('head')
def head(*args):
    title(*args)
    style(*args)

@mytag('body')
def body(*args):
    h1(*args)
    p(*args)

@mytag('style')
def style(*args):
    h1_color(*args)
    p_color(*args)

@mytag('title')
def title(*args):
    print(args[0], end="")

@mytag('h1_color')
def h1_color(*args):
    print(args[1], end="")

@mytag('p_color')
def p_color(*args):
    print(args[2], end="")

@mytag('h1')
def h1(*args):
    print(args[3], end="")

@mytag('p')
def p(*args):
    print(args[4], end="")

#hello(title_s, h1_color_s, p_color_s, h1_s, p_s)
hello(*input_data)
