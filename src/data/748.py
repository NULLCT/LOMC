import heapq

N, Q = map(int, input().split())
L = [[] * N for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    L[a - 1].append(b - 1)
    L[b - 1].append(a - 1)

from collections import deque

dist = [-1] * N
que = deque([0])
dist[0] = 0

while que:
    v = que.popleft()
    d = dist[v]
    for w in L[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        que.append(w)

for _ in range(Q):
    c, d = map(int, input().split())
    if c > d:
        c, d = d, c
    C = dist[c - 1]
    D = dist[d - 1]
    if (D - C) % 2 == 1:
        print('Road')
    else:
        print('Town')
