from string import ascii_lowercase
from decimal import Decimal
from random import randrange, choice, randint
import time
from heapq import heappop, heappush
from copy import copy
from bisect import bisect_right, bisect_left
from sys import stdin
from functools import reduce
from math import e, sqrt, gcd, pi, factorial, ceil, floor, sin
from itertools import permutations
from collections import defaultdict, deque, Counter
from enum import Enum, auto
import sys

sys.setrecursionlimit(1000000)

n, q = map(int, input().split())
to = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    to[a - 1].append(b - 1)
    to[b - 1].append(a - 1)

k = 1
while 2**k <= n - 1:
    k += 1
parent = [[-1 for _ in range(n)] for _ in range(k)]
dist = [-1 for _ in range(n)]

# def dfs(now, par, dis):
#     parent[0][now] = par
#     dist[now] = dis
#     for next in to[now]:
#         if next != par:
#             dfs(next, now, dis + 1)

visited = [False for _ in range(n)]
que = deque([(0, -1, 0)])
while que:
    now, par, dis = que.popleft()
    parent[0][now] = dis
    dist[now] = dis
    visited[now] = True
    for next in to[now]:
        if not visited[next]:
            que.append((next, now, dis + 1))

# dfs(0, -1, 0)

for i in range(k - 1):
    for j in range(n - 1):
        if parent[i][j] < 0:
            parent[i + 1][j] = -1
        parent[i + 1][j] = parent[i][parent[i][j]]


def query(u, v):
    if dist[u] < dist[v]:
        u, v = v, u
    for i in range(k):
        if (dist[u] - dist[v]) >> i & 1:
            u = parent[i][u]
    if u == v:
        return u
    for i in reversed(range(0, k)):
        if parent[i][u] != parent[i][v]:
            u = parent[i][u]
            v = parent[i][v]
    return parent[0][u]


for _ in range(q):
    c, d = map(int, input().split())
    par = query(c - 1, d - 1)
    dis = dist[c - 1] + dist[d - 1] - 2 * dist[par]
    if dis % 2 == 0:
        print("Town")
    else:
        print("Road")
