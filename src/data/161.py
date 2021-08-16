n, q = map(int, input().split())

from collections import deque

graph = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * n
dist[0] = 0

d = deque()
d.append(0)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

for i in range(q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
