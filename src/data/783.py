#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**7)
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from math import gcd
from functools import reduce
from operator import add, itemgetter, mul, xor
from heapq import heappush, heappop


def cmb(n, r, mod):
    bunshi = 1
    bunbo = 1
    for i in range(r):
        bunbo = bunbo * (i + 1) % mod
        bunshi = bunshi * (n - i) % mod
    return (bunshi * pow(bunbo, mod - 2, mod)) % mod


def I():
    return int(input())


def LI():
    return list(map(int, input().split()))


def MI():
    return map(int, input().split())


def LLI(n):
    return [list(map(int, input().split())) for _ in range(n)]


def LL(n):
    return [list(input()) for i in range(n)]


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


#bisect.bisect_left(list,key)はlistのなかでkey未満の数字がいくつあるかを返す
#つまりlist[i] < x となる i の個数
#bisect.bisect_right(list, key)はlistのなかでkey以下の数字がいくつあるかを返す
#つまりlist[i] <= x となる i の個数
#これを応用することで
#len(list) - bisect.bisect_left(list,key)はlistのなかでkey以上の数字がいくつあるかを返す
#len(list) - bisect.bisect_right(list,key)はlistのなかでkeyより大きい数字がいくつあるかを返す
#これらを使うときはあらかじめlistをソートしておくこと！

n, q = MI()
G = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = MI()
    G[a].append(b)
    G[b].append(a)
depth = [-1 for _ in range(n + 1)]


#depth[v]は頂点vの深さ
def dfs(graph, v, p=-1, d=0):
    depth[v] = d
    for next_v in graph[v]:
        if next_v == p:
            continue
        dfs(graph, next_v, v, d + 1)


dfs(G, 1)
for i in range(q):
    c, d = MI()
    size_c = depth[c]
    size_d = depth[d]
    if (size_c - size_d) % 2 == 0:
        print("Town")
    else:
        print("Road")
