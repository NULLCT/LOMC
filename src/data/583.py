# /usr/bin/python3
# -*- coding: utf-8 -*-
from bisect import bisect_left, bisect_right
from queue import Queue
from queue import LifoQueue as Stack
from math import sqrt, floor, ceil, log2, log10, pi, sin, cos, atan
from fractions import gcd
from itertools import permutations, combinations
from collections import Counter
from operator import itemgetter
from functools import cmp_to_key, reduce
from bisect import bisect_left

# INF=1001001001
# INF = 100010001000100010001
INF = float('INF')
__MOD__ = (10**9) + 7
yn = 'YNeos'
judge = False
cnt = 0
ans = None


def lcm(a, b):
    return (a * b) // gcd(a, b)


def intinput():
    return int(input())


def mulinputs():
    return map(int, input().split())


def lineinputs(func=intinput):
    datas = []
    while True:
        try:
            datas.append(func())
        except EOFError:
            break
    return datas


def bindex(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None


class UnionFind:
    def __init__(self, n):
        self.r = [-1] * (n + 1)

    def root(self, x):
        if self.r[x] < 0:
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.r[x] > self.r[y]:
            x, y = y, x
        self.r[x] += self.r[y]
        self.r[y] = x
        return True

    def size(self, x):
        return -1 * self.r[self.root(x)]


class ModInt():
    def __init__(self, x):
        self.__x = (x % __MOD__)

    def __add__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__((self.__x + other.__x) % __MOD__))
        elif type(other) == ModInt:
            return self.__class__((self.__x + other.__x) % __MOD__)
        else:
            raise Exception("Not Int or Not ModInt")

    def __radd__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__((other.__x + self.__x) % __MOD__))
        elif type(other) == ModInt:
            return self.__class__((other.__x + self.__x) % __MOD__)
        else:
            raise Exception("Not Int or Not ModInt")

    def __sub__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__((self.__x - other.__x) % __MOD__))
        elif type(other) == ModInt:
            return self.__class__((self.__x - other.__x) % __MOD__)
        else:
            raise Exception("Not Int or Not ModInt")

    def __rsub__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__((other.__x - self.__x) % __MOD__))
        elif type(other) == ModInt:
            return self.__class__((other.__x - self.__x) % __MOD__)
        else:
            raise Exception("Not Int or Not ModInt")

    def __mul__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__((self.__x * other.__x) % __MOD__))
        elif type(other) == ModInt:
            return self.__class__((self.__x * other.__x) % __MOD__)
        else:
            raise Exception("Not Int or Not ModInt")

    def __rmul__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__((other.__x * self.__x) % __MOD__))
        elif type(other) == ModInt:
            return self.__class__((other.__x * self.__x) % __MOD__)
        else:
            raise Exception("Not Int or Not ModInt")

    def __truediv__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__((self.__x * other.__modinv()) % __MOD__))
        elif type(other) == ModInt:
            return self.__class__((self.__x * other.__modinv()) % __MOD__)
        else:
            raise Exception("Not Int or Not ModInt")

    def __rtruediv__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__((other.__x * self.__modinv()) % __MOD__))
        elif type(other) == ModInt:
            return self.__class__((other.__x * self.__modinv()) % __MOD__)
        else:
            raise Exception("Not Int or Not ModInt")

    def __pow__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__(pow(self.__x, other.__x, __MOD__)))
        elif type(other) == ModInt:
            return self.__class__(pow(self.__x, other.__x, __MOD__))
        else:
            raise Exception("Not Int or Not ModInt")

    def __rpow__(self, other):
        if type(other) == int:
            other = self.__class__(other)
            return int(self.__class__(pow(other.__x, self.__x, __MOD__)))
        elif type(other) == ModInt:
            return self.__class__(pow(other.__x, self.__x, __MOD__))
        else:
            raise Exception("Not Int or Not ModInt")

    def __modinv(self, m=__MOD__):
        a = self.__x
        if a == 0:
            raise ZeroDivisionError()
        if gcd(a, m) != 1:
            raise Exception("%sの逆数は求まりません。" % a)
        b, u, v = m, 1, 0
        while b != 0:
            t = a // b
            a -= t * b
            a, b = b, a
            u -= t * v
            u, v = v, u
        u %= m
        if u < 0:
            u += m
        return u

    def __int__(self):
        return self.__x

    def __str__(self):
        return str(self.__x)


if __name__ == '__main__':
    N, Q = mulinputs()
    paths_list = []
    for _ in range(N):
        paths_list.append(set())

    for _ in range(N - 1):
        a, b = mulinputs()
        paths_list[a - 1].add(b - 1)
        paths_list[b - 1].add(a - 1)

    indatas = []
    for _ in range(Q):
        c, d = mulinputs()
        indatas.append((c - 1, d - 1))

    s, e = 0, N - 1
    q = Queue()
    q.put(s)

    count = []
    for _ in range(N):
        count.append(-1)
    count[s] = 0

    while not q.empty():
        v = q.get()
        for path in paths_list[v]:
            if count[path] < 0:
                count[path] = 1 - count[v]
                q.put(path)

    for s, e in indatas:
        if (count[e] - count[s]) % 2 == 0:
            print('Town')
        else:
            print('Road')
    exit()

#     for s, e in indatas:
#         q = Queue()
#         q.put(s)
#         count = []
#         for _ in range(N):
#             count.append(0)
#         count[s] = 1
#         visited = set()
#         visited.add(s)
#         while not q.empty():
#             v = q.get()
#             if e in paths_list[v]:
#                 count[e] = count[v] + 1
#                 break
#             for path in paths_list[v]:
#                 if path in visited:
#                     continue
#                 count[path] = count[v] + 1
#                 q.put(path)
#                 visited.add(path)
#
#         if count[e] % 2 == 1:
#             print(f"Town")
#         else:
#             print(f"Road")
