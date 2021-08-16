#!/usr/bin/env python3
import itertools
import sys

sys.setrecursionlimit(10**7)  #再帰回数の上限変更
import collections
from collections import deque
import copy
import bisect

inf = int(1e9)

n, q = map(int, input().split())

road = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)

C = []
D = []
for i in range(q):
    c, d = map(int, input().split())
    C.append(c - 1)
    D.append(d - 1)

Dist = [inf for _ in range(n)]


def bfs():
    que = deque()
    que.append(0)
    Dist[0] = 0

    while len(que) != 0:
        p = que.popleft()
        for i in road[p]:
            if Dist[i] == inf:
                que.append(i)
                Dist[i] = Dist[p] + 1
    return


bfs()

for i in range(q):
    tmp = (Dist[C[i]] - Dist[D[i]]) % 2
    if tmp == 1:
        print("Road")
    else:
        print("Town")
