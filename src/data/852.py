from collections import deque

n, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

CD = []
for i in range(q):
    e, f = map(int, input().split())
    CD.append([e, f])

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

for i, j in CD:
    x = dist[i] + dist[j]
    if x % 2 == 0:
        print("Town")
    else:
        print("Road")
