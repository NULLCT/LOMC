from collections import deque

n, q = map(int, input().split())
g = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    g[b - 1].append(a - 1)
    g[a - 1].append(b - 1)

dist = [-1] * n
dist[0] = 0
queue = deque()
queue.append(0)

while len(queue) != 0:
    v = queue.popleft()
    for i in g[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        queue.append(i)

for i in range(q):
    c, d = map(int, input().split())
    if dist[c - 1] % 2 != dist[d - 1] % 2:
        print("Road")
    else:
        print("Town")
