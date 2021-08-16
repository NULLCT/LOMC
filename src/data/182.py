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

colors = [-1 for _ in range(n)]

que = deque([(0, 0)])
while que:
    node, color = que.popleft()
    colors[node] = color
    for next_node in to[node]:
        if colors[next_node] == -1:
            que.append((next_node, color ^ 1))

# def dfs(now, c):
#     assert c in [0, 1]
#     colors[now] = c
#     for next in to[now]:
#         if colors[next] == -1:
#             dfs(next, c ^ 1)

# dfs(0, 0)
assert -1 not in colors

for _ in range(q):
    c, d = map(int, input().split())
    if colors[c - 1] == colors[d - 1]:
        print("Town")
    else:
        print("Road")
