import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math
from decimal import Decimal
import copy
import random

# from fractions import gcd

MOD = 10**9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)

n, q = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

dis = [-1] * n
dis[0] = 0
que = deque([(0, 0)])
while que:
    e, d = que.popleft()
    for nxt in G[e]:
        if dis[nxt] != -1:
            continue
        dis[nxt] = d + 1
        que.append((nxt, d + 1))

# print(dis)

for i in range(q):
    c, d = map(int, input().split())
    if (dis[c - 1] + dis[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
