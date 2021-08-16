from collections import deque

N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]

G = [[] for _ in range(N)]

for i in range(N - 1):
    ai, bi = map(int, ab[i])
    G[ai - 1].append(bi - 1)
    G[bi - 1].append(ai - 1)

color = [0] * N
color[0] = -1

d = deque()
d.append(0)

while d:
    v = d.popleft()
    for i in G[v]:
        if color[i] != 0:
            continue
        color[i] = -color[v]
        d.append(i)

for j in range(Q):
    cj, dj = map(int, input().split())
    if color[cj - 1] == color[dj - 1]:
        print('Town')
    else:
        print('Road')
