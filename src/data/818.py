n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

from collections import deque

dist = [-1] * n  # 頂点1からの最短距離distance
dist[0] = 0
d = deque()
d.append(0)

while d:
    v = d.popleft()
    for i in g[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

# print(*dist)

for j in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if abs(dist[d] - dist[c]) % 2 == 0:
        print('Town')
    else:
        print('Road')
