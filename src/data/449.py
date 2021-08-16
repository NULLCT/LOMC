from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

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

lis = [0] * n

for i in range(n):
    if dist[i] % 2 == 0:
        lis[i] = 1
    else:
        lis[i] = -1
out = [0] * m
for i in range(m):
    a, b = map(int, input().split())
    if lis[a - 1] == lis[b - 1]:
        out[i] = "Town"
    else:
        out[i] = "Road"
for i in out:
    print(i)
