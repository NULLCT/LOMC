from collections import deque

N, P = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dist = [-1] * N
Q = deque()
Q.append(0)
dist[0] = 0
while Q:
    now = Q.popleft()
    for to in G[now]:
        if dist[to] == -1:
            dist[to] = dist[now] + 1
            Q.append(to)

for _ in range(P):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    L = dist[c] + dist[d]
    if L % 2 == 0:
        print("Town")
    else:
        print("Road")
