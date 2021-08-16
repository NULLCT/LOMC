from sys import stdin
from collections import deque

readline = stdin.readline
n, q = map(int, readline().split())
graph = [[] for _ in range(n)]
visited = [-1] * n
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
stack = deque([])
stack.append([0, -1])
visited[0] = 1
while stack:
    v, p = stack.pop()
    if visited[v] == -1:
        if p != -1:
            if visited[p] == 0:
                visited[v] = 1
            else:
                visited[v] = 0
    for e in graph[v]:
        if e == p:
            continue
        stack.append([e, v])
for j in range(q):
    c, d = map(int, readline().split())
    if visited[c - 1] == visited[d - 1]:
        print('Town')
    else:
        print('Road')
