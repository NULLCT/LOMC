import sys


# input = sys.stdin.readline
def mp():
    return map(int, input().split())


def lmp():
    return list(map(int, input().split()))


def mps(A):
    return [tuple(map(int, input().split())) for _ in range(A)]


import math
import bisect
from copy import deepcopy as dc
from itertools import accumulate
from collections import Counter, defaultdict, deque


def ceil(U, V):
    return (U + V - 1) // V


def modf1(N, MOD):
    return (N - 1) % MOD + 1


inf = int(1e20)
mod = int(1e9 + 7)
import heapq


def dijkstra(start, edge):
    # edge[i] = [(distance, j), ...]
    dist = [int(1e18)] * len(edge)
    dist[start] = 0
    q = [(0, start)]
    while q:
        c, u = heapq.heappop(q)
        if dist[u] < c: continue
        for v, nc in edge[u]:
            if (dist[u] + v) < dist[nc]:
                dist[nc] = dist[u] + v
                heapq.heappush(q, (dist[nc], nc))
    return dist


n, q = mp()
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = mp()
    a -= 1
    b -= 1
    edge[a].append((1, b))
    edge[b].append((1, a))
u = dijkstra(0, edge)
for i in range(q):
    a, b = mp()
    if abs(u[a - 1] - u[b - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
