import sys
from collections import deque

N, Q = map(int, input().split())
M = N - 1

g = {i: set() for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

dist = {i: sys.maxsize for i in range(1, N + 1)}
v = {i: False for i in range(1, N + 1)}

que = deque([1])
dist[1] = 0
while que:
    nd = que.popleft()
    v[nd] = True
    for ch in g[nd]:
        dist[ch] = min(dist[nd] + 1, dist[ch])
        if not v[ch]:
            que.append(ch)

for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[c] + dist[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
