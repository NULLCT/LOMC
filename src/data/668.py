from collections import defaultdict
from collections import deque

N, Q = list(map(int, input().split()))
G = defaultdict(lambda: [])

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# G[v]: 頂点vに隣接する頂点list
# N: 頂点数

dist = [-1] * N
que = deque([0])
dist[0] = 0
while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        que.append(w)

for _ in range(Q):
    c, d = list(map(int, input().split()))
    if dist[c - 1] % 2 == dist[d - 1] % 2:
        print('Town')
    else:
        print('Road')
