import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, q = map(int, input().split())
graph = []
INF = 10**9
for i in range(n):
    graph.append([])
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
dist = [INF] * n
curr = 0
stack = [(0, 0)]
while stack:
    a, pos = stack.pop()
    dist[pos] = a
    for i in graph[pos]:
        if dist[i] == INF:
            stack.append((a + 1, i))
for i in range(q):
    c, d = map(int, input().split())
    if dist[c - 1] % 2 == dist[d - 1] % 2:
        print('Town')
    else:
        print('Road')
