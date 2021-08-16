#!/usr/bin/env python
import sys

sys.setrecursionlimit(10**9)

n, q = map(int, input().split())
c = [0 for _ in range(q)]
d = [0 for _ in range(q)]
to = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

for i in range(q):
    c[i], d[i] = map(int, input().split())
    c[i] -= 1
    d[i] -= 1

depth = [0 for _ in range(n)]


def dfs(v, d, p=-1):
    depth[v] = d
    for u in to[v]:
        if u != p:
            dfs(u, d + 1, v)


dfs(0, 0)

for i in range(q):
    if abs(depth[c[i]] - depth[d[i]]) % 2 == 1:
        print('Road')
    else:
        print('Town')
