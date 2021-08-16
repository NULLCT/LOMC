N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
from collections import deque

dist = [-1] * (N)
dist[0] = 0  #start地点を0とする
d = deque()
d.append(0)
while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)
for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2:
        print('Road')
    else:
        print('Town')
