n, q = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

#0 or 1
color = [-1 for _ in range(n)]
color[0] = 0

#bfs
from collections import deque

queue = deque()
queue.append(0)
while queue:
    v = queue.popleft()
    for nei in graph[v]:
        if color[nei] == -1:
            color[nei] = 1 - color[v]
            queue.append(nei)

for _ in range(q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
