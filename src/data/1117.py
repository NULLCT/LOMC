N, Q = map(int, input().split())
G = [[] for _ in range(N)]
from collections import deque

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

dist = [-1] * N
dist[0] = 0

d = deque()
d.append(0)

while d:
    v = d.popleft()
    for i in G[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

for i in range(Q):
    c, e = map(int, input().split())
    if (dist[c - 1] - dist[e - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")

#print(dist)
