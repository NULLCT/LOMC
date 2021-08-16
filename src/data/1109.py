from collections import deque

n, q = map(int, input().split())

G = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int,
               input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1] * n
que = deque()

dist[0] = 0
que.append(0)

while que:
    v = que.popleft()

    for nv in G[v]:
        if dist[nv] != -1: continue

        dist[nv] = dist[v] + 1
        que.append(nv)

for i in range(q):
    c, d = map(int, input().split())
    t = abs(dist[c - 1] - dist[d - 1])
    if t % 2 == 1:
        print("Road")
    else:
        print("Town")
