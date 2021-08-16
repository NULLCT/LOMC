#!/usr/bin/env python3
from itertools import accumulate, chain, combinations, groupby, permutations, product
from collections import deque, Counter
from bisect import bisect_left, bisect_right
from math import gcd, sqrt, sin, cos, tan, degrees, radians, ceil, floor
from fractions import Fraction
from decimal import Decimal
import sys

n, q = map(int, input().split())
g = [[] for _ in range(n)]  # 隣接リスト


#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
def bfs(u):
    queue = deque([u])
    d = [None] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


MOD = 10**9 + 7
INF = float('inf')


#float型の無限大inf
def resolve():
    #n=int(input())

    for _ in range(n - 1):
        a, b = [int(x) for x in input().split()]
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    #C = list(map(int, input().split()))
    #C.sort()
    #d=bfs(1)
    #print(d)
    d = bfs(0)
    for i in range(q):
        c, doo = map(int, input().split())

        if (d[c - 1] - d[doo - 1]) % 2 == 1:
            print("Road")
        else:
            print("Town")


if __name__ == "__main__":
    resolve()
