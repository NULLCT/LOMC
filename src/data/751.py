from collections import deque

n, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
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
for i in range(n + 1):
    dist[i] = dist[i] % 2
for i in range(q):
    c, d = map(int, input().split())
    if dist[c] == dist[d]:
        print('Town')
    else:
        print('Road')
