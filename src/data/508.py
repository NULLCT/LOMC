import sys
from collections import defaultdict, deque

n, q = map(int, sys.stdin.buffer.readline().split())

graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.buffer.readline().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

colors = [-1] * n
colors[0] = 0

que = deque([0])
while que:
    v = que.popleft()
    for w in graph[v]:
        if colors[w] == -1:
            colors[w] = 1 - colors[v]
            que.append(w)

for _ in range(q):
    c, d = map(int, sys.stdin.buffer.readline().split())
    c, d = c - 1, d - 1
    if colors[c] == colors[d]:
        print('Town')
    else:
        print('Road')
