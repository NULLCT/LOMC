from collections import deque

N, Query = map(int, input().split())

G = []
for _ in range(N):
    G.append([])
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

while len(Q) > 0:

    i = Q.popleft()

    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)

for i in range(N):
    if dist[i] % 2 == 0:
        dist[i] = 1
    else:
        dist[i] = 2

for _ in range(Query):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] == dist[d]:
        print('Town')
    else:
        print('Road')
