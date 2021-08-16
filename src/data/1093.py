import itertools as iter
import collections as coll
import heapq as hq
import bisect as bis
from decimal import Decimal as dec
from copy import deepcopy as dcopy
import math
import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def getN():
    return int(input())


def getNs():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))


def strinps(n):
    return [input() for _ in range(n)]


pi = 3.141592653589793
mod = 10**9 + 7
MOD = 998244353
INF = math.inf
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
"""
Main Code
"""

n, q = getNs()
route = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = getNs()
    a -= 1
    b -= 1
    route[a].append(b)
    route[b].append(a)
query = [getList() for _ in range(q)]
time = [INF] * n
que = [(1, 0)]
while (que):
    t, v = que.pop()
    time[v] = t
    for nv in route[v]:
        if (time[nv] > t + 1):
            que.append((t + 1, nv))

for c, d in query:
    c -= 1
    d -= 1
    if ((time[c] - time[d]) & 1):
        print("Road")
    else:
        print("Town")
