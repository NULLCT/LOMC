from collections import deque

n, Q = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

dist = [-1] * n
q = deque([0])
dist[0] = 0

while q:
    now = q.popleft()
    for nxt in edges[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

for _ in range(Q):
    c, d = map(int, input().split())
    if dist[c - 1] % 2 == dist[d - 1] % 2:
        print("Town")
    else:
        print("Road")