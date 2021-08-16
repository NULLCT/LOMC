n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)
cd = [list(map(int, input().split())) for _ in range(q)]
from collections import deque


def bfs():
    q = deque()
    dist = [-1] * n
    q.append(0)
    dist[0] = 0
    while q:
        v = q.popleft()
        for v1 in g[v]:
            if dist[v1] == -1:
                dist[v1] = dist[v] + 1
                q.append(v1)
    return dist


dist = bfs()
for c, d in cd:
    if (dist[c - 1] - dist[d - 1]) % 2 == 1:
        print('Road')
    else:
        print('Town')
