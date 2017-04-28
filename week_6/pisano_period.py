__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = 10 ** 18
m = 10 ** 5

# n = 10
#m = 4


#x = 1.61803398874989 ** n
#x = int((1.61803398874989 ** n / 2.23606797749979) + 0.5) % m
# print(x)
# print(int((1.61803398874989 ** n / 2.23606797749979) + 0.5))

def fib_calc_n(n):
    n_1Fib = 1
    n_2Fib = 1
    nFib = 1
    if (n == 0):
        return 0
    elif (n < 2):
        return 1
    else:
        for i in range(1, n - 1):
            nFib = (n_1Fib + n_2Fib)
            n_2Fib = n_1Fib
            n_1Fib = nFib
        return nFib


def fib_calc(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


def find_count_pisano_period(m):
    s = []
    a = k = 0
    b = 1
    while s[k:k + 4] != s[:4] or k < 1:
        s.append(a % m)
        k = len(s) // 2
        a, b = b, a + b
    return k

def find_pisano_period(m):
    i = 0
    deep = 4
    s = [0, 1]
    while s[i-deep:i] != s[:deep] or i-deep < 1:
        s.append((s[i + 1] + s[i]) % m)
        i += 1
    return s[:i-deep]


def v1(n, m):
    pisano_period = find_pisano_period(m)
    print(pisano_period[n % len(pisano_period)])


# def v1(n, m):
#     period_pisano = find_count_pisano_period(m)
#     nFib_period_pisano = n % period_pisano
#     print(fib_calc_n(nFib_period_pisano) % m)



def v2(n, m):
    k = 0
    s = [0, 1]
    for i in range(2, n):
        s.append((s[i - 1] + s[i - 2]) % m)
        k = k + 1
        if (S[i] == 1) and (S[i - 1] == 0):
            break
        if k > 0 and s[k:k+4] == [0, 1, 1, 2]:
            break
    print(s[(n % k)], len(s))


# if (n - m < 100):
#     v1(n, m)
# else:
#     v2(n, m)

v1(n, m)

# # print('=======')
# for i in range(12):
#     print(fib_calc(i) % 5, i, fib_calc(i))
#
# print(10 % 6)