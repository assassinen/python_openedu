__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-



print(sum(range(1,6)))

n = 20
x = sum(range(1,n+1))
for i in range(19):
    x -= 1
    print(x)

def adding (a):
    a = list(a)
    n = 0
    while a[0:1] != a[-1:] and n < 100:
        a[0] += 1
        a[1] += 1
        a.sort()
        n += 1
    return a[0:1] == a[-1:]

a = [
    (2, 3, 6, 7, 8),
    (1, 2, 3, 4),
    (1, 2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5)
]

# for i in a:
#     print(adding(i))
#
# for i in a:
#     print(not(len(i) % 2 == 0 and sum(i) % 2 != 0), sum(i) % len(i) % 2, sum(i) % len(i), sum(i), sum(i) % 2)

b = (
    (3, 1, 2),
    (1, 3, 2),
    (1, 2, 3),
    (2, 3, 1),
    (3, 2, 1),
    (2, 1, 3),
    )


def combo(a):
    x = 0
    y = 0
    for i in a:
        for j in a[a.index(i)+1:]:
            if i > j:
                x += 1
        # print(x-y)
    y = x
    #return x
    return x % 2 == 0

print("====")
# print(combo((1,2,3,4,6,5)))
# print(combo((5,13,3,7,11,14,6,9,12,2,15,4,8,1,10)))
#
for i in b:
    print(combo(i))

r = 1
d = 1
# for i in range(1,121):
#     r += 1
#     d += 2
#     print(i, r, d)