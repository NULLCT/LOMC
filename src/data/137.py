from collections import deque

n, q = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
color = [False] * n
dist = [-1] * n
#町xからの距離の偶奇を記録する
dist[0] = 0
d = deque()
d.append(0)
while d:
    v = d.popleft()
    for i in G[v]:
        if dist[i] != -1:
            continue
        dist[i] = (dist[v] + 1) % 2
        d.append(i)
for i in range(q):
    c, d = map(int, input().split())
    if dist[c - 1] == dist[d - 1]:
        print('Town')
    else:
        print('Road')
