# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().strip()


import math
import collections
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect
from copy import deepcopy
import itertools
from heapq import heappush, heappop, heapify
import statistics

INF = 10**20
mod = 10**9 + 7
from decimal import Decimal
import string
# import numpy as np
# alp = list(string.ascii_letters[0:26])
# map(int,input().split())


def dijkstra(start, n):  # (始点, ノード数)
    dist = [-1] * n
    hq = [(0, start)]  # (distance, node)
    dist[start] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if (seen[to] == False
                    and dist[v] + cost < dist[to]) or (seen[to] == False
                                                       and dist[to] == -1):
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


# ノード数, エッジ数, 始点ノード, 終点ノード
# n,m,x,y = map(int, input().split())
n, q = map(int, input().split())
m = n - 1

# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((b, 1))
    adj[b].append((a, 1))

dis_k = dijkstra(0, n)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    print("Town" if (dis_k[c] + dis_k[d]) % 2 == 0 else "Road")
