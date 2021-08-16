# 頂点N、重みなしの木を構成する
N, Q = map(int, input().split())
edge = [[] for i in range(N)]
for i in range(1, N):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

# bfs:幅優先探索
from collections import deque

que = deque()
que.append(0)
dist = [-1] * N
dist[0] = 0
while que:
    now = que.pop()
    for nex in edge[now]:
        if dist[nex] == -1:
            dist[nex] = dist[now] + 1
            que.append(nex)

for i in range(Q):
    c, d = map(int, input().split())
    ans = "Town"
    if dist[c - 1] % 2 != dist[d - 1] % 2:
        ans = "Road"
    print(ans)
