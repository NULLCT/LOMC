#!/usr/bin/env python3
from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

s = 0
dist = [-1] * N
que = deque()
que.append(s)
dist[s] = 0
while que:
    i = que.popleft()
    for j in G[i]:
        if dist[j] == -1:
            dist[j] = 1 - dist[i]
            que.append(j)

for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if dist[c] == dist[d]:
        print("Town")
    else:
        print("Road")
