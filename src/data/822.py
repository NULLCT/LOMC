# BFS, breadth first search, 幅優先探索
from collections import defaultdict, deque

N, Q = map(int, input().split())
# 隣接リストはdefaultdictで管理すると楽
G = defaultdict(lambda: [])

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

INF = 10**18
dist = [INF] * N
parent = [-1] * N  # 親ノード
q = deque()

dist[0] = 0
q.append(0)
while q:
    now = q.popleft()  # now: 探索起点
    for to in G[now]:  # to: 隣接リストの接続先
        if dist[to] != INF:  # toをすでに探索していたらINFではない。
            continue
        dist[to] = dist[now] + 1  # 距離の更新
        parent[to] = now
        q.append(to)

out = []
for i in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if abs(dist[a] - dist[b]) % 2 == 1:
        out.append("Road")
    else:
        out.append("Town")
print(*out, sep="\n")
