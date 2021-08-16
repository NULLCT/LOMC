#!/usr/bin/env python3
from collections import deque


def wfs(num):
    q = deque([[num, 0]])
    while q:
        k, d = q.popleft()
        for i in G[k]:
            if depth[i] == -1:
                depth[i] = d + 1
                q.append([i, depth[i]])
    return


N, Q = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a] += [b]
    G[b] += [a]

depth = [-1] * N
depth[0] = 0

wfs(0)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    delta = abs(depth[c] - depth[d]) % 2

    if delta == 0:
        print("Town")
    else:
        print("Road")
