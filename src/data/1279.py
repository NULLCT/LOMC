# 二部グラフで塗る: 典型のやつ
from collections import deque

n, q = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

color = [-1 for i in range(n)]
color[0] = 1
que = deque([0])
while que:
    v = que.popleft()
    for u in G[v]:
        if color[u] == -1:
            color[u] = 1 - color[v]
            que.append(u)

for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if color[c] == color[d]: print('Town')
    else: print('Road')
