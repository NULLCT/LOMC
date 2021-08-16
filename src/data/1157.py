from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
dist = [-1] * N
D = deque()
dist[0] = 0
D.append(0)
while D:
    v = D.popleft()
    for nv in G[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            D.append(nv)
for i in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
