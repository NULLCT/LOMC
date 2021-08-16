N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
cd = [list(map(int, input().split())) for _ in range(Q)]

G = [[] for _ in range(N)]
for a, b in ab:
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1 for _ in range(N)]
dist[0] = 0

from collections import deque

Qu = deque()
Qu.append(0)

while len(Qu) > 0:
    i = Qu.popleft()

    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Qu.append(j)
for c, d in cd:
    c -= 1
    d -= 1
    diff = dist[c] - dist[d]
    if diff % 2 != 0:
        print('Road')
    else:
        print('Town')
