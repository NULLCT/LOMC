from collections import deque

n, q = map(int, input().split())
G = [[] for i in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
dist = [-1] * n
dist[0] = 0
Q = deque([0])
while Q:
    u = Q.popleft()
    for v in G[u]:
        if dist[v] == -1:
            Q.append(v)
            dist[v] = dist[u] + 1
for _ in range(q):
    c, d = map(int, input().split())
    print("Road" if (dist[c - 1] - dist[d - 1]) % 2 else "Town")
