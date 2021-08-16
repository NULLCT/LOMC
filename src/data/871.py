from collections import deque

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1 for i in range(N)]
dist[0] = 0

q = deque([])
q.append((0, 0))

while q:
    p, d = q.popleft()
    for g in G[p]:
        if dist[g] == -1:
            dist[g] = d + 1
            q.append((g, d + 1))
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
