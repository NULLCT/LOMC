#!/usr/bin/env python3
# from typing import *

import sys
import io
import math
import collections
import decimal
import itertools
import bisect
import heapq


def input():
    return sys.stdin.readline()[:-1]


sys.setrecursionlimit(1000000)

# _INPUT = """4 1
# 1 2
# 2 3
# 2 4
# 1 2

# """
# sys.stdin = io.StringIO(_INPUT)

INF = 10**10

# class RunTree:
#     depth = []
#     eular_tour = []
#     in_time = []
#     _data = []
#     _N1 = 0
#     def __init__(self, G) -> None:
#         N = len(G)
#         self.eular_tour = []
#         self.in_time = [0] * N
#         self.depth = [-1] * N
#         seen = [False] * N
#         self._dfs(G, seen, 0, 0)
#         # Segment tree
#         self._N1 = 2 **(len(self.eular_tour)-1).bit_length()
#         self._data = [(-10**10, None)] * (2 * self._N1)
#         for i, v in enumerate(self.eular_tour):
#             self._data[self._N1+i] = (self.depth[v], v)
#         for i in reversed(range(1, self._N1)):
#             self._data[i] = min(self._data[2*i], self._data[2*i+1])
#     def _dfs(self, G, seen, p, depth):
#         seen[p] = True
#         self.in_time[p] = len(self.eular_tour)
#         self.depth[p] = depth
#         self.eular_tour.append(p)
#         for p1 in G[p]:
#             if p1 == p or seen[p1]:
#                 continue
#             self._dfs(G, seen, p1, depth+1)
#             self.eular_tour.append(p)
#     def get_lca(self, u, v):
#         l = self.in_time[u] + self._N1
#         r = self.in_time[v] + self._N1
#         if l > r:
#             l, r = r, l
#         r += 1
#         res = (10**10, None)
#         while l < r:
#             if l & 1:
#                 res = min(res, self._data[l])
#                 l += 1
#             if r & 1:
#                 res = min(res, self._data[r-1])
#                 r -= 1
#             l //= 2
#             r //= 2
#         return res[1]

# def dfs(parent, p, d):
#     depth[p] = d
#     for p1 in G[p]:
#         if p1 == parent:
#             continue
#         dfs(p, p1, d+1)

N, Q = map(int, input().split())
G = [list() for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

depth = [-1] * N
seen = [False] * N
q = collections.deque()
q.append(0)
seen[0] = True
depth[0] = 0
while q:
    p = q.pop()
    for p1 in G[p]:
        if seen[p1]:
            continue
        seen[p1] = True
        depth[p1] = depth[p] + 1
        q.appendleft(p1)

result = []
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    l = depth[c] + depth[d]
    if l % 2 == 0:
        result.append('Town')
    else:
        result.append('Road')
print('\n'.join(result))
