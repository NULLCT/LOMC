n, q = map(int, input().split())

from collections import deque

m = n - 1

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

for i in range(q):
    x, y = map(int, input().split())
    ans = dist[y] - dist[x]
    if ans % 2 == 0:
        print('Town')
    else:
        print('Road')
